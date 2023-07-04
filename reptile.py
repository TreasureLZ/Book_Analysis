import requests
from bs4 import BeautifulSoup
import time
def fun(find,type=None):
    if find:
        if type:
            try:
                return find[0].get(type).strip().replace('\t','').replace('\n','')
            except:
                return ""
        return find[0].text.strip().replace('\t','').replace('\n','')
def getData(url,data,category):
    headers = {
        'Cookie':'ddscreen=2; __permanent_id=20230409115645877132444186122226077; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; ad_ids=13863640%2C3521297%2C13863708%2C13863691%2C3225928%2C16603271%2C12141595%2C3225935%2C3272556%2C7556590%2C3627134%2C3554365%2C2723462%2C3226022%2C3226013%2C3225953%2C3225922%2C3225874%2C3521294%2C3521274%2C3225970%2C3225834%2C3225915%2C3226010%7C%233%2C3%2C3%2C3%2C1%2C1%2C2%2C2%2C1%2C1%2C2%2C2%2C1%2C3%2C3%2C3%2C3%2C3%2C1%2C1%2C1%2C1%2C1%2C1; __rpm=s_605253.4516872..1681031897096%7Cs_605253.4516872..1681031916733; search_passback=f3e5d57e2c4c4f57ec82326400000000f3826500cf823264; pos_9_end=1681031919141; pos_6_start=1681031919171; pos_6_end=1681031919184',
        'Host': 'category.dangdang.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    
    li_list = soup.select('#search_nature_rg ul.bigimg li')
    for li in li_list:
        title = fun(li.select('a.pic'),'title').split('（')[0]
        author = li.select('p.search_book_author span')[0].text.strip().replace('\t','').replace('\n','')
        createTime = li.select('p.search_book_author span')[1].text.strip().replace('\t','').replace('\n','')
        press = li.select('p.search_book_author span')[2].text.strip().replace('\t','').replace('\n','')
        now_price = fun(li.select('p.price span.search_now_price'))
        pre_price = fun(li.select('p.price span.search_pre_price'))
        discount = fun(li.select('p.price span.search_discount'))
        detail = fun(li.select('p.detail'))
        star = fun(li.select('p.search_star_line span.search_star_black span'),'style')
        comment_num = fun(li.select('p.search_star_line a.search_comment_num'))
        img_url = fun(li.select('.pic img'),'data-original')
        if img_url:
            img_url = "http:" + img_url
        book_url = fun(li.select('p.name a'),'href')
        if book_url:
            book_url = "http:" + book_url    
        addTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        data.append([category,title,author,createTime,press,now_price,pre_price,discount,detail,star,comment_num,img_url,book_url,addTime])
        
def writeData(data):
    with open('./data.csv','w+',encoding='utf-8') as fp:
        fp.write("\t".join(['category','title','author','createTime','press','now_price','pre_price','discount','detail','star','comment_num','img_url','book_url','addTime'])+'\n')
        for item in data:
            fp.write("\t".join([str(i) for i in item])+'\n')
            
if __name__ == '__main__':
    base = 'http://category.dangdang.com/pg{}-cp01.{}.00.00.00.00.html'
    data = []
    # 这个设置爬取多少页
    max_page = 10
    category_code = {'成功/励志':'21','艺术':'07','历史':'36','文学':'05','医学':'56','计算机/网络':'54','经济':'25','社会科学':'30','科普读物':'52','时尚/美妆':'11','哲学/宗教':'28','建筑':'55'}
    for category in category_code:
        for page in range(max_page):
            url  = base.format(page+1,category_code[category])
            try:
                getData(url,data,category)
                print('类别{}第{}页爬取成功!'.format(category,page+1))
                time.sleep(1)
            except:
                print('类别{}第{}页爬取失败!'.format(category,page+1))
                time.sleep(15)
    writeData(data)
    