# -*- coding:utf-8 -*-

import requests
import re
import json
from requests.exceptions import RequestException
import time

def get_one_page(url):
    """
    获取每页的网页源代码
    :param url: 请求链接
    :return: 网页的文本内容
    """
    try:
        headers = {
            'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
        }
        response = requests.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding
        #print(response.content)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    """
    使用正则表达式解析网页数据
    :param html: 网页的文本内容
    :return: 字典
    """
    pattern = re.compile(
        r'<\w*?><a href="([^\\\'#\"]*?)" target="_blank">(\D*?)</a></li>',
        re.S
    )
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'local': item[0],
            'title': item[1].replace('\"', '\''),
        }


def write_to_file(content):
    with open('smh.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')



def main(offset):
    url = 'http://www.piyao.org.cn/index.htm'.format(str(offset))
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)


if __name__ == '__main__':
    open('smh.txt', 'w', encoding='utf-8')
    for i in range(1):
        main(offset=i * 10)
        time.sleep(1)
