
import json
import os
class Aistant_Chat_Setting():
    def __init__(self):
        print("Aistant_Setting init.")

#UI选项补全元素管理
        self.chat_model_dict = [
        {'company':'openai', 'model':'gpt-3.5-turbo', 'type': 'Chat'},
        {'company':'openai', 'model':'gpt-3.5-turbo-0301', 'type': 'Chat'},
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

# 默认的setting content设置
        self.aistant_json_default_content  =   {'role': 0,\
                                                'model': 0,
                                                'muitl_chat': True,
                                                'custom_role': '',
                                                'cur_key_value': '',
                                                'his_key_value': [],
                                                }
#本地保存管理
        self.aistant_setting_file_path = 'setting.json'
        self.aistant_check_local_setting_and_update_cache()

    # 软件启动时，检查并在必要时更新 setting 文件
    def aistant_check_local_setting_and_update_cache(self):
        content = self.aistant_get_content_by_json_file()
        # TODO: 增加必要的合法性检查, 比如key少的情况下，需要与默认配置进行合并补全
        if content == '':
            self.aistant_recover_with_default_setting()
            return
        self.aistant_json_tempory_content = content

    # 获取 settin.json的content内容
    def aistant_get_content_by_json_file(self):
        content = ''
        if os.path.isfile(self.aistant_setting_file_path):
            print("配置存在")
            with open(self.aistant_setting_file_path, 'r') as f:
                try:
                    content = json.load(f)
                except ValueError as e:
                    print("配置不合法，将setting.json恢复为默认配置")
        else:
            print("配置不存在，将setting.json恢复为默认配置")
        return content

    # 将setting.json 恢复为软件内部的默认配置
    def aistant_recover_with_default_setting(self):
        print("aistant_recover_with_default_setting")
        with open(self.aistant_setting_file_path, 'w') as f:
            json.dump(self.aistant_json_default_content, f)
        self.aistant_json_tempory_content = self.aistant_json_default_content

    def aistant_update_local_file_with_content(self):
        print("aistant_update_local_file_with_content")
        with open(self.aistant_setting_file_path, 'w') as f:
            json.dump(self.aistant_json_tempory_content, f)

# --------------访问(读/写) local setting的相关方法 ------------------#
    def aistant_setting_get_role_id(self):
        try:
            role_val = self.aistant_json_tempory_content['role']
        except:
            role_val = -1
        return role_val

    def aistant_setting_set_role_id(self, role_id):
        print("aistant_setting_set_role_id")
        ret = 0
        try:
            self.aistant_json_tempory_content['role'] = role_id
            # self.aistant_update_local_file_with_content()
        except:
            self.aistant_json_tempory_content['role'] = 0
            # self.aistant_update_local_file_with_content()
            ret = -1
        self.aistant_update_local_file_with_content()
        return ret

    def aistant_setting_get_model_id(self):
        try:
            model_val = self.aistant_json_tempory_content['model']
        except:
            model_val = -1
        return model_val
    
    def aistant_setting_set_model_id(self, model_id):
        ret = 0
        try:
            self.aistant_json_tempory_content['model'] = model_id
        except:
            self.aistant_json_tempory_content['model'] = 0
            ret = -1
        self.aistant_update_local_file_with_content()
        return ret
    
    def aistant_setting_get_multi_chat(self):
        try:
            multi_chat_val = self.aistant_json_tempory_content['muitl_chat']
        except:
            multi_chat_val = 'error'
        return multi_chat_val

    def aistant_setting_set_multi_chat(self, multi_chat_state):
        print("aistant_setting_set_multi_chat")
        ret = 0
        try:
            self.aistant_json_tempory_content['muitl_chat'] = multi_chat_state
        except:
            self.aistant_json_tempory_content['muitl_chat'] = True
            ret = -1 
        self.aistant_update_local_file_with_content()
        return ret

    def aistant_setting_get_cur_key_val(self):
        try:
            cur_key_val = self.aistant_json_tempory_content['cur_key_value']
        except:
            cur_key_val = 'error'
        return cur_key_val
    
    def aistant_setting_set_cur_key_val(self, key_val):
        ret = 0
        try:
            print("aistant_setting_set_cur_key_val: ", key_val)
            self.aistant_json_tempory_content['cur_key_value'] = key_val
        except:
            print("aistant_setting_set_cur_key_val. Empty.")
            self.aistant_json_tempory_content['cur_key_value'] = ''
            ret = -1
        self.aistant_update_local_file_with_content()
        return ret
    
    def aistant_setting_get_his_key_val(self):
        try:
            his_key_val = self.aistant_json_tempory_content['his_key_value']
        except:
            his_key_val = 'error'
        return his_key_val

# --------------------------- UI元素补全 ---------------------------#
# 获取对话角色及描述UI补全
    def aistant_select_role_and_descript_get_config(self):
        return self.role_default_config_dict

# 设置对话模型
    def aistant_chat_model_dict_get_config(self):
        return self.chat_model_dict
    
    def aistant_chat_model_dict_get_idx_by_model(self, model):
        for idx, model_name in enumerate(self.chat_model_dict):
            print(idx, model_name)
            if model_name['model'] == model:
                return idx

if __name__ == "__main__":
    print("Aistant setting manage")
    aistant_setting = Aistant_Chat_Setting()