# KnowledgeGraphCode
用来存放学习知识图谱的时候的代码

## 环境要求
```
pip install pyahocorasick -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install pandas
pip install py2neo==4.3.0 -i https://pypi.douban.com/simple
pip install pyltp
```
说明，对于pyltp的话，应该pip是装不上的，https://pypi.tuna.tsinghua.edu.cn/simple/pyltp-binary/
应该在这个网址上直接下载对应版本的whl进行安装。
## Python2neo
这个文件夹用来存放一个简单的，包含了创建节点和关系的一个小项目，直接运行invoice_neo4j.py即可


## QAMedicalKG
这个是一个基于知识图谱的医药问答的代码实战。
注意，medical2.json是一个toy版本的，可以跑代码快一点。
不过在进行问答的阶段，就需要首先用medical.json用完整的预料构建知识图谱了，这
要花很久的时间。。。。。
运行answer_search是进行问答的，速度也很慢。


