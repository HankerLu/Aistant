

class Aistant_Chat_Setting():
    def __init__(self):
        print("Aistant_Setting init.")
        self.chat_model_dict = [
        {'company':'openai', 'model':'gpt-3.5-turbo', 'type': 'Chat'},
        {'company':'openai', 'model':'text-davinci-003', 'type': 'Complete'},
        {'company':'openai', 'model':'text-curie-001', 'type': 'Complete'},
        {'company':'openai', 'model':'text-babbage-001', 'type': 'Complete'},
        {'company':'openai', 'model':'text-ada-001', 'type': 'Complete'},
        {'company':'openai', 'model':'text-davinci-002', 'type': 'Complete'},
        {'company':'openai', 'model':'text-davinci-001', 'type': 'Complete'},
        {'company':'openai', 'model':'davinci-instruct-beta', 'type': 'Complete'},
        {'company':'openai', 'model':'davinci', 'type': 'Complete'},
        {'company':'openai', 'model':'curie-instruct-beta', 'type': 'Complete'},
        {'company':'openai', 'model':'curie', 'type': 'Complete'},
        {'company':'openai', 'model':'babbage', 'type': 'Complete'},
        {'company':'openai', 'model':'ada', 'type': 'Complete'}, 
        ]
        self.role_default_config_dict = [
        {'role':'助手', 
         'brief':'我希望你能扮演一名得力的助手的角色。'},
        {'role':'翻译', 
         'brief':'我希望你能担任英语翻译、拼写校正和改进者的角色。我会用任何语言与你交谈，你将检测语言，翻译它，并用更美丽优雅、高级、文学化的英语单词和句子来回答我的文本,但保持意思相同。我希望你只回答修正和改进，没有其他解释。我的第一句话是“我喜欢伊斯坦布尔，这里很美好”。'},
        {'role':'广告商', 
         'brief':'我希望你能扮演一个广告商的角色。您需要创建一个针对18-30岁的年轻人的新型能量饮料的广告活动。您需要选择目标受众，制定关键信息和口号，选择推广的媒体渠道，并决定任何其他必要的活动以实现您的目标。'},
        {'role':'辩手', 
         'brief':'我希望你能扮演辩手的角色。我会提供一些与当前事件相关的主题，你的任务是研究辩论的双方，提出有效的论点，驳斥对立观点，并基于证据得出有说服力的结论。你的目标是帮助人们从讨论中获得更多的知识和洞察力。我的第一个请求是“我想要一篇关于Deno的观点文章”。'},
        {'role':'自定义', 
         'brief':'自定义'},
        ]

        self.multi_round_chat_config = True

# 设置对话角色及描述
    # def aistant_select_role_and_descript_set_config(self, role_descript_dict):
    #     print("Aistant select role and descript set config.")
    #     self.role_default_config_dict = role_descript_dict

    def aistant_select_role_and_descript_get_config(self):
        return self.role_default_config_dict

# 设置多轮对话模式
    def aistant_multi_round_chat_set_config(self, enable):
        print("Aistant multi round set config")
        self.multi_round_chat_config = enable

    def aistant_multi_round_chat_get_config(self):
        return self.multi_round_chat_config

# 设置对话模型
    # def aistant_chat_model_dict_set_config(self, model_dict):
    #     self.chat_model_dict = model_dict

    def aistant_chat_model_dict_get_config(self):
        return self.chat_model_dict

# 设置密钥