import Aistant_UI_agent
import Aistant_func

if __name__ == "__main__":
    aistant_ui = Aistant_UI_agent.Aistant_UI_Agent()
    aistant_chat_core = Aistant_func.Aistant_Chat_Core()

    aistant_ui.aistant_ui_set_chat_submit_cb_ptr(aistant_chat_core.chat_core_button_submit_exec)
    aistant_ui.aistant_ui_set_chat_clear_cb_ptr(aistant_chat_core.chat_core_button_clear_exec)
    aistant_ui.aistant_ui_set_chat_cancel_cb_ptr(aistant_chat_core.chat_core_button_cancel_exec)
    aistant_ui.aistant_ui_set_chat_save_cb_ptr(aistant_chat_core.chat_core_button_save_exec)
    aistant_ui.aitant_ui_activate_button()

    aistant_chat_core.chat_core_set_get_input_text_cb_ptr(aistant_ui.aistant_ui_get_input_textedit_exec)
    aistant_chat_core.chat_core_set_display_response_cb_ptr(aistant_ui.aistant_ui_display_txt_output_exec)
    aistant_chat_core.chat_core_set_save_chat_cb_ptr(aistant_ui.aistant_ui_save_current_chat_exec)
    aistant_chat_core.chat_core_set_update_statusbar_cb_ptr(aistant_ui.aistant_ui_update_statusbar_txt)

    aistant_ui.Aistant_UI_show()
