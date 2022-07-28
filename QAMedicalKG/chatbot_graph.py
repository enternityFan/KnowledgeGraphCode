# @Time : 2022-07-28 15:20
# @Author : Phalange
# @File : chatbot_graph.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D

from QAMedicalKG.question_classifier import *
from QAMedicalKG.question_parser import *
from QAMedicalKG.answer_search import *


"""问答类"""

class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self,sent):
        answer = "没能理解您的问题，我数据量有限。。。。。能不能问的标准点"
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer

        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.format(final_answers)


if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        """
        胸闷可能导致的症状
        肺气肿吃什么好呢？
        """
        question = input('咨询:')
        answer = handler.chat_main(question)
        print('客服机器人:', answer)


