# -*- coding: utf-8 -*-
# @Time : 2022/5/25 13:18
# @Author : AMan

from lxml import etree

xml = """
<book>
    <id>11</id>
    <name>《老鼠的自我修养》</name>
    <price>8.88</price>
    <author>
        <nick id="aman">阿瞒</nick>
        <nick id="2">yjc</nick>
    </author>
    <parent>活着</parent>
    <div>
        <author>
            <nick id="aman2">阿瞒2</nick>
            <nick id="22">yjc2</nick>
        </author>
        <parent>活着2</parent>
    </div>
</book>
"""

tree = etree.XML(xml)
print(tree)
# result = tree.xpath("/book")
# result = tree.xpath("/div/*/nick/text()")  # []
# result = tree.xpath("/book/author")
# result = tree.xpath("/book/author/nick/text()")  # ['阿瞒', 'yjc'] /text()获取数据
# result = tree.xpath("/book//nick/text()")  # ['阿瞒', 'yjc', '阿瞒2', 'yjc2'] 所有后代//
# result = tree.xpath("/book/*/*/nick/text()")  # ['阿瞒2', 'yjc2'] 通配符*

# result = tree.xpath("/book/*/*/nick[1]/text()")  # ['阿瞒2'] nick[1]获取第一个，索引从1开始

# result = tree.xpath("/book/author/nick[@id='aman']/text()")  # ['阿瞒'] 通过属筛选
# print(result)

result = tree.xpath("/book//nick")  # ['阿瞒', 'yjc', '阿瞒2', 'yjc2'] 所有后代//
for i in result:
    print(i)
    # 从每一个nick中提取信息
    print(i.xpath("./text()"))  # 使用./继续查找
    print(i.xpath("./@id"))  # 查找标签属性的id值
    print("-------------------")
