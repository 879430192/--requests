# xpath : 一种在XML文档中搜索内容的一种语言
# html是xml的一个子集

"""
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <author>
        <nick>周大强</nick>
        <nick>周芷若</nick>
    </author>
</book>
"""

# 安装xml模块  pip install lxml
# xpath解析

from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <author>
        <nick>周大强</nick>
        <nick>周芷若</nick>
    </author>
</book>
"""
tree = etree.XML(xml)
# result = tree.xpath("/book")  # /表示层级关系。第一个/是根节点
# result = tree.xpath("/book/name")
# result = tree.xpath("/book/name/text()")  #text() :拿到文本
# result = tree.xpath("/book/author//nick/text()")  # // 所有节点下的后代
# result = tree.xpath("/book/author/*/nick/text()")   # * ：任意的节点，通配符
result = tree.xpath("/book//nick/text()")

print(result)
