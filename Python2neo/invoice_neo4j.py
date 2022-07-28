# @Time : 2022-07-28 12:42
# @Author : Phalange
# @File : invoice_neo4j.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


from Python2neo.DataToNeo4jClass import DataToNeo4j
import os
import pandas as pd


invoice_data = pd.read_excel('./Invoice_data_Demo.xls', header=0,)

def data_extraction():
    """节点数据抽取"""
    node_buy_key = []
    for i in range(0,len(invoice_data)):
        node_buy_key.append(invoice_data['购买方名称'][i])

    node_sell_key = []
    for i in range(0,len(invoice_data)):
        node_sell_key.append(invoice_data['销售方名称'][i])

    # 去除重复的发票名称
    node_buy_key = list(set(node_buy_key))
    node_sell_key = list(set(node_sell_key))

    # value 抽出作node
    node_list_value = []
    for i in range(0,len(invoice_data)):
        for n in range(1,len(invoice_data.columns)):
            node_list_value.append(invoice_data[invoice_data.columns[n]][i])

    # 去重
    node_list_value = list(set(node_list_value))
    # 将list的浮点和整数都转换为字符串类型
    node_list_value = [str(i) for i in node_list_value]

    return node_buy_key,node_sell_key,node_list_value


def relation_extraction():
    """ 联系数据抽取"""
    links_dict = {}
    sell_list = []
    money_list = []
    buy_list = []

    for i in range(0,len(invoice_data)):
        # 将数据中int类型全部转换为string
        money_list.append(str(invoice_data[invoice_data.columns[19]][i]))
        sell_list.append(str(invoice_data[invoice_data.columns[10]][i]))
        buy_list.append(str(invoice_data[invoice_data.columns[6]][i]))


    # 整合数据，把三个list整合成一个dict
    links_dict['buy'] = buy_list
    links_dict['money'] = money_list
    links_dict['sell'] = sell_list
    # 把数据转成dataFrame类型
    df_data = pd.DataFrame(links_dict)
    print(df_data)

    return df_data


relation_extraction()
create_data = DataToNeo4j()


create_data.create_node(data_extraction()[0],data_extraction()[1])
create_data.create_relation(relation_extraction())



