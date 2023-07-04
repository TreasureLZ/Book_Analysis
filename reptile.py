import requests
from bs4 import BeautifulSoup
import re
import jieba
import pandas as pd
import time
import collections
import pymysql
from sqlalchemy import create_engine

#爬虫获取产品ID
def get_cpid (keyword):
    url=f'http://www.zyctd.com/Search/Index?keyword={keyword}'
    #获取网页数据
    res=requests.get(url)
    #编码
    res.encoding = 'utf-8'
    #解析网页数据
    soup = BeautifulSoup(res.text, 'lxml')
    #通过正则表达式返回要的数据
    reg=re.compile('(?<=gongxiao).*?(?=.html)')
    #对返回值进行数据提取。拿到产品ID
    cpid = reg.findall(str(soup.find('li','hover')))[0]
    return cpid

def get_yf_fun(cpid,ys=0):
    # 请求地址
    url = 'https://www.zyctd.com/api/data-service/api/v1/product/getTcmPrescriptionPage'
    # 设置tcmid=cpid,设置药方数量每次为100个，
    j = {"init": 0, "tcmId": cpid, "nameAndIndications": '', "years": "0",
         "pageRequest": {"pageNumber": ys+1, "pageSize": 100}}
    # 根据要求构造请求头文件
    headers = {
        "Content-Type": "application/json;charset=utf8",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Referer": "https://www.zyctd.com/data/zzjf.html?id=75"
    }
    # 得到链接的内容
    res = requests.post(url, json=j, headers=headers)
    # 编码
    res.encoding = 'utf-8'
    # 将返回值转化为元组，方便提取
    return eval(res.text)

def get_yf_totalRows(cpid):
    result=get_yf_fun(cpid,1)
    if result['code']==0:
        totalRows=result['data']['totalRows']
        print(f"共有{totalRows}个药方")
        return totalRows
    else:
        print('获取药方数量失败')
        
# 获取药方清单  
def get_yf_list(cpid,totalRows,keyword):
    datas = {
        'uid': [],
        'name': [],
        'recipe': [],
        'dosage': [],
        'excerpt': [],
        'indications': [],
        'note': [],
        'processing':[],
        'tcmName': [],
        'recipe_pz': [],
    }
    counts = {}
    print(f"系统将分成{totalRows // 100 + 1}页获取药方")
    # 去除一些语气词和没有意义的词
    del_words = ['的', ' ', '克', '两', 'g', '千克', '钱', '斤','毫升','浸一宿','两钱','各克']
    # 除100（每次取100个药方）向下取整然后+1，遍历所有药方清单
    for row_i in range(totalRows // 100 + 1):
        print(f'开始获取第{row_i+1}页药方')
        result=get_yf_fun(cpid,row_i)
        for res in result['data']['pageContent']:
            if ('克' in res['recipe']) or ('g' in res['recipe']) or('钱' in res['recipe']) or('斤' in res['recipe'])or('两' in res['recipe']):
                datas['uid'].append(res['id'])
                datas['dosage'].append(res['dosage'])
                datas['excerpt'].append(res['excerpt'])
                datas['indications'].append(res['indications'])
                datas['name'].append(res['name'])
                datas['note'].append(res['note'])
                datas['processing'].append(res['processing'])
                datas['recipe'].append(res['recipe'])
                datas['tcmName'].append(res['tcmName'])
                # 对药方进行处理
                # 去掉标点符号
                all_quotes = re.sub(r"[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+", "", res['recipe'])
                # 结巴分词自动切割，得到每个药方有什么药材
                words = jieba.lcut(all_quotes)
                words_final = []
                # 如果词不在即将去除的内容中，就添加
                for word in words:
                    if word not in del_words and len(word)>1:
                        words_final.append(word)
                        counts[word] = counts.get(word, 0) + 1
                datas['recipe_pz'].append(words_final)
        #把药方药材存到excel
        pd_datas=pd.DataFrame(datas)
        pd_datas.to_excel(f'./data/{keyword}药方.xlsx',index=None)

    print(f"经过排除后，共获取到{len(datas['uid'])}个药方")
    
def get_yc_scjg(keyword,cpid):
    url=f'https://www.zyctd.com/jh{cpid}.html'
    # 根据要求构造请求头文件
    headers = {
        "Content-Type": "application/json;charset=utf8",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    }

    # 得到链接的内容
    res = requests.get(url, headers=headers)
    # 编码
    res.encoding = 'utf-8'
    # 解码
    soup = BeautifulSoup(res.text, 'lxml')
    tbody_s = soup.find('table', class_='tableBase').find('tbody').find_all('tr')  # 寻找 zixun-item 类型的类
    cd_s=[]
    jg_s=[]
    for tbody in tbody_s:
        td_s=tbody.find_all('td')
        cd=td_s[1].text
        jg=td_s[2].text.replace('￥','')
        cd_s.append(cd)
        jg_s.append(float(jg))
    
    with open("./data/{}产地价格.csv".format(keyword),'w+',encoding='utf-8') as fp:
        fp.write("keyword\torigin\tprice\n")
        for idx in range(len(cd_s)):
            fp.write(keyword+'\t'+cd_s[idx]+"\t"+str(jg_s[idx])+"\n")

    #通过正则表达式返回要的数据
    reg=re.compile('(?<=historyPriceMID = parseInt\(\").*?(?=\"\);)')
    mid = reg.findall(str(soup))[0]

    #这个mid在获取历史价格的时候需要
    return  mid

def get_yc_jg(ycmc,cpid,mid):
    # 请求地址
    url = 'https://www.zyctd.com/Breeds/GetPriceChart'

    # # 设置mid=mid，
    j = {"mid": mid,
         "PriceType":"day"}
    # 根据要求构造请求头文件
    headers = {
        "Content-Type": "application/json;charset=utf8",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Referer": f"https://www.zyctd.com/jh{cpid}.html"
    }
    # 得到链接的内容
    res = requests.post(url,json=j , headers=headers)
    # 编码
    res.encoding = 'utf-8'
    # 将返回值转化为元组，方便提取,存在null 需要替换
    jg_s=eval(res.text.replace("null", '""'))['Data']['PriceChartData']
    #对字符串形返回值进行处理
    jg_s=jg_s.replace('[','').replace(']','')
    jg_arr=jg_s.split(',')
    #循环每一天的价格
    x=[]
    y=[]
    #循环近30天价格
    day=30
    for i in range(day):
        #时间戳转化为日期
        time_jg = time.localtime(int(jg_arr[len(jg_arr)-2*day+2*i]) / 1000)
        dt = time.strftime("%Y-%m-%d", time_jg)
        # print(jg_arr[-(2*i+1)])
        x.append(dt)
        y.append(jg_arr[len(jg_arr)-2*day+2*i+1])
    with open('./data/{}历史价格.csv'.format(keyword),'w+',encoding='utf-8') as fp:
        fp.write("keyword\tupdateTime\tprice\n")
        for idx in range(len(x)):
            fp.write(keyword+'\t'+x[idx]+'\t'+str(y[idx])+'\n')
   
def get_yc_cd_url(cpid,ys):
    url=f'https://www.zyctd.com/gqgy/{cpid}-0-p{ys}.html'
    print(f'正在获取第{ys}页药材供应内容数据')
    # 根据要求构造请求头文件
    headers = {
        "Content-Type": "application/json;charset=utf8",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Referer": "https://www.zyctd.com/jh75.html"
    }

    # 得到链接的内容
    res = requests.get(url, headers=headers)
    # 编码
    res.encoding = 'utf-8'
    return res.text 

#获得药材产地
def get_yc_cd(keyword,cpid):
    sl_s=[]
    kcd_s=[]
    cd_s=[]
    #获取前10页药材供应内容。每页10个产品
    for i in range(10):
        res_data=get_yc_cd_url(cpid,i+1)
        # 解码
        soup = BeautifulSoup(res_data, 'lxml')
        div_name_list = soup.find_all('div', class_='supply_list')  # 寻找 supply_list 类型的类
        for div_name in div_name_list:
            #数量
            sl=div_name.find_all('li')[1].find('span').text
            #排除供应数量少于吨的
            if '吨' not  in sl:
                continue
            sl_s.append(sl.replace('吨',''))
            #库存地
            kcd=div_name.find_all('li')[2].find('span').text
            kcd_s.append(kcd)
            #产地
            cd=div_name.find_all('li')[3].find('span').text
            cd_s.append(cd)
    #准备数据
    cd_arr=[]
    cd_cd_sl_arr=[]
    for cd_s_i in range(len(cd_s)):
        cd_sl=0
        for cd_s_j in range(cd_s_i+1,len(cd_s)):
            if cd_s[cd_s_i] not in cd_arr and cd_s[cd_s_i]==cd_s[cd_s_j]:
                cd_sl+=int(sl_s[cd_s_j])
        if cd_s[cd_s_i] not in cd_arr:
            cd_arr.append(cd_s[cd_s_i])
            cd_sl+=int(sl_s[cd_s_i])
            cd_cd_sl_arr.append((cd_s[cd_s_i],cd_sl))

    result_sort = sorted(cd_cd_sl_arr, key=lambda x: x[1], reverse=True)  # 排序
    result_sort = collections.OrderedDict(result_sort)
    othervalue = 0
    for i in range(5, len(cd_cd_sl_arr)):
        othervalue += list(result_sort.values())[i]
    values = []
    labels = []
    for i in range(5):
        values.append(list(result_sort.values())[i])
        labels.append(list(result_sort.keys())[i])
    values.append(othervalue)
    labels.append('其他产地')
    with open('./data/{}药材供应产地.csv'.format(keyword),'w+',encoding='utf-8') as fp:
        fp.write("keyword\torigin\tcount\n")
        for idx in range(len(values)):
            fp.write(keyword+'\t'+labels[idx]+'\t'+str(values[idx])+'\n')

def get_yc_sczixun_url(cpid,ys):
    url = f'https://www.zyctd.com/zixun/202/pz{cpid}-{ys}.html'
    print(f'正在获取第{ys}页数据')
    # 根据要求构造请求头文件
    headers = {
        "Content-Type": "application/json;charset=utf8",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Referer": "https://www.zyctd.com/jh75.html"
    }

    # 得到链接的内容
    res = requests.get(url, headers=headers)
    # 编码
    res.encoding = 'utf-8'
    return res.text

def  get_yc_sczixun(keyword,cpid):
    zx_title=[]
    zx_content=[]
    #获取前10页药材市场资讯。每页10个资讯
    for i in range(10):
        res_data=get_yc_sczixun_url(cpid,i+1)
        # 解码
        soup = BeautifulSoup(res_data, 'lxml')
        dl_name_list = soup.find_all('dl', class_='zixun-item')  # 寻找 zixun-item 类型的类
        for dl_name in dl_name_list:
            title = dl_name.select("dt a span")[0].text.strip().replace('\n','').replace('\t','').replace(' ','')
            content = dl_name.select("div.item-content p.content-text.g-clearfix span")[0].text.strip().replace('\n','').replace('\t','').replace(' ','')
            zx_title.append(title)
            zx_content.append(content)

    with open('./data/{}药材市场资讯.csv'.format(keyword),'w+',encoding='utf-8') as fp:
        fp.write("keyword\ttitle\tcontent\n")
        for i in range(len(zx_title)):
            title = zx_title[i]
            content = zx_content[i]
            print(title,type(title))
            print(content,type(content))
            if not title:
                continue
            elif not content:
                continue
            elif len(content) < 50:
                continue
            elif "BORDER-BOTTOM" in content:
                continue
            elif "spanstyle" in content:
                continue
            else:
                s = keyword+'\t'+title+'\t'+content+'\n'
                if len(s) < 50:
                    continue
                else:
                    fp.write(s)

def writeData(keyword):
    engine = create_engine("mysql+pymysql://root:Llb011223@localhost:3306/materialsDB?charset=utf8")

    df = pd.read_excel('./data/{}药方.xlsx'.format(keyword))
    df.to_sql('prescript', con=engine, if_exists='append', index=False)

    df = pd.read_csv('./data/{}产地价格.csv'.format(keyword),sep='\t')
    df.to_sql('originprice', con=engine, if_exists='append', index=False)

    df = pd.read_csv('./data/{}历史价格.csv'.format(keyword),sep='\t')
    df.to_sql('historyprice', con=engine, if_exists='append', index=False)

    df = pd.read_csv('./data/{}药材供应产地.csv'.format(keyword),sep='\t')
    df.to_sql('originstatistics', con=engine, if_exists='append', index=False)

    df = pd.read_csv('./data/{}药材市场资讯.csv'.format(keyword),sep='\t')
    df.dropna(axis=0, how='any', inplace=True)
    df.to_sql('info', con=engine, if_exists='append', index=False)


if __name__ == '__main__':
    keyword=input('请输入您要搜索什么药材(柴胡)：')
    # 获取药材ID
    cpid=get_cpid(keyword)
    # 获取药方数量
    totalRows=get_yf_totalRows(cpid)
    # 获取药方清单 
    get_yf_list(cpid,totalRows,keyword)
    # 获取药材市场价格
    mid=get_yc_scjg(keyword,cpid)
    # 获得药材的价格
    get_yc_jg(keyword,cpid,mid)
    # 获取药材供应产地
    get_yc_cd(keyword,cpid)
    # 获取药材市场资讯
    get_yc_sczixun(keyword,cpid)
    writeData(keyword)


