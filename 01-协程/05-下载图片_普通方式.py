# -- coding: utf-8 --
# @Time : 2022/8/12 9:37
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 05-下载图片_普通方式.py
# @Software: PyCharm


import requests


# 下载三张图片

def download_image(url):
    print("开始下载", url)
    # 发送网络请求，下载图片
    response = requests.get(url)
    print("下载完成")

    # 图片保存到本地文件
    file_name = url.rsplit('/')[-1]
    print(file_name)

    with open(file_name, mode='wb') as file_objects:
        file_objects.write(response.content)


if __name__ == '__main__':
    url_list = ["http://img.netbian.com/file/2022/0810/2210450pka0.jpg",
                "http://img.netbian.com/file/2022/0720/004410CGAKF.jpg",
                "http://img.netbian.com/file/2022/0712/234912VQcQL.jpg"]

    for item in url_list:
        download_image(item)



