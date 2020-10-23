import requests
from lxml import etree

# with open('movie.txt','r') as fp:
#     txt = fp.read()

url = 'http://www.mca.gov.cn//article/sj/xzqh/2020/2020/2020092500801.html'
txt = requests.get(url).text
tree = etree.HTML(txt)
trs = tree.xpath('//tr')[3:-9]

clean_trs = []
for tr in trs:
    txt_list = tr.xpath('.//text()')
    per = []
    for j in txt_list:
        if j.strip() != '':
            per.append(j)
    clean_trs.append(per)

result = {'data':[]}

for txt_list in clean_trs:
    prov_num = txt_list[0][:2]
    city_num = txt_list[0][2:4]
    county_num = txt_list[0][4:]
    if city_num == '00' and county_num == '00':
        prov = {'code':txt_list[0], 'name':txt_list[1],'province':txt_list[0],'city':'','country':''}  #省
    if city_num != '00' and county_num == '00':
        prov = {'code': txt_list[0], 'name': txt_list[1],'province':txt_list[0][:2] + '0000' ,'city': txt_list[0], 'country': ''}  #市
    if city_num != '00' and county_num != '00':
        prov = {'code': txt_list[0], 'name': txt_list[1], 'province': txt_list[0][:2] + '0000', 'city': txt_list[0][:4]+'00','country': txt_list[0]}  #县

    result['data'].append(prov)
    # print(prov)

print(result)
