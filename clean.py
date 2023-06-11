import pandas as pd
import re
from sqlalchemy import create_engine
#显示所有列，把行显示设置成最大
pd.set_option('display.max_columns', None)
#显示所有行，把列显示设置成最大
pd.set_option('display.max_rows', None)

df = pd.read_csv('data.csv',sep='\t',encoding='utf-8',dtype = {'star' : str,'title': str,'author' : str,'detail' : str})

# 重复值处理
print("重复值去除前数据量为：{}".format(len(df)))
df.drop_duplicates(inplace=True)
print("清洗后数据量为：{}".format(len(df)))

# 缺失值处理
print("缺失值去除前数据量为：{}".format(len(df)))
df.dropna(axis=0,how='any',inplace=True)
print("清洗后数据量为：{}".format(len(df)))

# 发行时间清洗（createTime）
df['createTime'] = df['createTime'].apply(lambda x:x.replace('/',''))

# 出版社清洗（press）
df['press'] = df['press'].apply(lambda x:x.replace('/',''))

# 优惠清洗（discount）
def clean_discount(discount):
    if discount == 'None':
        return ""
    return discount.replace(')','').replace('(','')
df['discount'] = df['discount'].apply(clean_discount)

# 评分清洗（star）
def clean_star(star):
    star = "".join(re.findall('[0-9]',star))
    if not star:
        return 0
    return star
df['star'] = df['star'].apply(clean_star)

# 评论数量清洗
def clean_comment_num(comment_num):
    comment_num = "".join(re.findall('[0-9]',comment_num))
    if not comment_num:
        return 0
    return comment_num
df['comment_num'] = df['comment_num'].apply(clean_comment_num)

# 价格清洗
def clean_price(price):
    return "".join(re.findall('[0-9.]',price))
df['now_price'] = df['now_price'].apply(clean_price)
df['pre_price'] = df['pre_price'].apply(clean_price)

# 折扣清洗
def clean_discount(discount):
    discount = "".join(re.findall('[0-9.]',discount))
    if discount == '':
        return 0
    return discount
df['discount'] = df['discount'].apply(clean_discount)

# 书名清洗（title）
def clean_title(title):
    return "".join(re.findall('[\u4e00-\u9fa5a-zA-Z0-9 ]',title))
df['title'] = df['title'].apply(clean_title)

# 作者清洗（author）
def clean_author(author):
    return "".join(re.findall('[\u4e00-\u9fa5a-zA-Z0-9 ]',author))
df['author'] = df['author'].apply(clean_author)

# 详情清洗（detail）
def clean_detail(detail):
    if len(detail) >= 400:
        return ""
    return "".join(re.findall('[\u4e00-\u9fa5]',detail))
df['detail'] = df['detail'].apply(clean_detail)

# 清洗完的文件写出
df.to_csv('./clean_data.csv',sep='\t',index=False)

# 创建数据库引擎，配置信息
engine = create_engine("mysql+pymysql://root:Llb011223@localhost:3306/booksdb?charset=utf8")

# 存入数据库
df.to_sql('booktable', con=engine, if_exists='append', index=False)