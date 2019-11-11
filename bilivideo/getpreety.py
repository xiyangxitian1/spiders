# -*- coding: utf-8 -*-
import json
import requests
import time
from urllib import parse
import pymysql
import re
import os

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

# 请求图片时使用的header
header1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}


def answer(url_):
    r = requests.get(url_, headers=header)
    data = r.text
    jsonobj = json.loads(data)
    return jsonobj


url = "https://www.zhihu.com/api/v4/questions/266808424/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&offset={}&limit=10&sort_by=default&platform=desktop" \
    .format(10)
# 获取回答总数
answer_total = int(answer(url)['paging']['totals'])
offset = 0
while offset < answer_total:
    url = "https://www.zhihu.com/api/v4/questions/266808424/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&offset={}&limit=10&sort_by=default&platform=desktop" \
        .format(offset * 10)
    offset += 1
    print(offset)
    answer_row = answer(url)
    data = answer_row['data']
    # voteup_count = data[0].voteup_count
    # print("voteup_count:" + voteup_count)
    if data.__len__ == 0:
        break
    else:
        for index, data_ in enumerate(data):
            voteup_count = data[index]['voteup_count']
            #  根据点赞的数量选出点赞多的
            if voteup_count < 20000:
                break
            # 答主的知乎主页
            author_url = "https://www.zhihu.com/people/" + \
                         data[index]['author']['url_token'] + "/activities"
            # 答主的性别
            author_gender = data[index]['author']['gender']
            # 回答正文
            answer_content = data[index]['content']
            # print(author_url)
            # 使用正则获取图片URL
            img_urls = re.findall('src=\"(https://.*?)"', answer_content)
            # 去除重复的URL
            img_urls = list(set(img_urls))
            # print(json.dumps(img_urls))
            # 回答中没有图片，跳过
            if img_urls.__len__() == 0:
                break
            else:
                for img_url in img_urls:
                    print('imgUrl:' + img_url)
                    # if isinstance(img_url, list):
                    #     for img_url_zi in img_url:
                    #         print('zi:'+img_url_zi)

                    time.sleep(1)
