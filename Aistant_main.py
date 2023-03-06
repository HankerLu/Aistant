import Aistant_UI_agent
import Aistant_func

if __name__ == "__main__":
    aistant_core = Aistant_func.Aistant_Backend_Func()
    aistant_ui = Aistant_UI_agent.Aistant_UI_Agent()
    aistant_ui.Aistant_UI_show()
    # ui.action_chatgpt.triggered.connect(print_text_by_q_action) # type: ignore

    # MainWindow.show()
    # sys.exit(app.exec_())
