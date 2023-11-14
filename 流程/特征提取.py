#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   特征提取.py
@Author  :   Cat 
@Version :   3.11
"""

import jieba
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def dict_demo():
    """
    字典特征提取
    :return: None
    """
    # 1.获取数据
    data = [
        {"city": "北京", "temperature": 100},
        {"city": "上海", "temperature": 60},
        {"city": "深圳", "temperature": 30},
    ]

    # 2.字典特征提取
    # 2.1 实例化
    transfer = DictVectorizer(sparse=True)

    # 2.2 转换
    new_data = transfer.fit_transform(data)
    print(new_data)

    # 2.3 获取具体属性名
    names = transfer.get_feature_names_out()
    print(f"属性:{names}")


def english_count_demo():
    """
    文本特征提取-英文
    :return: None
    """
    # 获取数据
    data = ["life is is short,i like python",
            "life is too long,i dislike python"]

    # 文本特征转换
    # transfer = CountVectorizer(sparse=True)  # 注意:没有sparse这个参数
    transfer = CountVectorizer(stop_words=["dislike"])
    new_data = transfer.fit_transform(data)

    # 查看特征名字
    names = transfer.get_feature_names()

    print("特征名字是:\n", names)
    print(new_data.toarray())
    print(new_data)


def chinese_count_demo1():
    """
    文本特征提取-中文
    :return: None
    """
    # 获取数据
    data = ["人生 苦短，我 喜欢 Python", "生活 太长久，我 不喜欢 Python"]

    # 文本特征转换
    transfer = CountVectorizer()
    new_data = transfer.fit_transform(data)

    # 查看特征名字
    names = transfer.get_feature_names()

    print("特征名字是:\n", names)
    print(new_data.toarray())
    print(new_data)


def cut_word(text):
    """
    中文分词
    :param text:
    :return:
    """
    # ret = " ".join(list(jieba.cut(text)))
    # print(ret)
    return " ".join(list(jieba.cut(text)))


def chinese_count_demo2():
    """
    文本特征提取-中文
    :return: None
    """
    # 1.获取数据
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]

    # 2.文章分割
    list = []
    for temp in data:
        list.append(cut_word(temp))
    print(list)

    # 3.文本特征转换
    # 3.1 实例化+转化
    transfer = CountVectorizer(stop_words=["一种", "今天"])
    new_data = transfer.fit_transform(list)

    # 3.2 查看特征名字
    names = transfer.get_feature_names()

    print("特征名字是:\n", names)
    print(new_data.toarray())
    print(new_data)


def tfidf_demo():
    """
    文本特征提取-中文
    :return: None
    """
    # 1.获取数据
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]

    # 2.文章分割
    list = []
    for temp in data:
        list.append(cut_word(temp))
    print(list)

    # 3.文本特征转换
    # 3.1 实例化+转化
    transfer = TfidfVectorizer()
    new_data = transfer.fit_transform(list)

    # 3.2 查看特征名字
    names = transfer.get_feature_names()

    print("特征名字是:\n", names)
    print(new_data.toarray())
    print(new_data)

if __name__ == "__main__":
    dict_demo()