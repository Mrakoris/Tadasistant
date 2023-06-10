import openai
from PySide6.QtWidgets import QMessageBox

import MainWindow


class chatAnswers(object):
    def __init__(self):
        super().__init__()

openai.api_key = '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'

messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]


def check_topic_filter(message):
    allowed_topics = ["РФ", "Рф", "рф", "федеральные законы", "федеральных законов", "правительства РФ", "кодекс",
                      "Закон РФ о", "закон РФ о", "закон рф о", "акты РФ", "президента РФ", "акты рф", "президента рф",
                      "министерства", "министерство", "федеральные органы исполнительной власти",
                      "конституционный суд РФ",
                      "судебная практика", "судебной практики", "региональное", "правовые акты", "бухгалтерскому учету",
                      "бухгалтерского учета", "бух учету", "бух учета", "ФСБУ", "управленческий учет",
                      "управленческого учета",
                      "отчетность", "отчетности", "регистры", "счета", "счетов", "финансковая отчетность",
                      "финансовой отчетности",
                      "налоговый учет", "налогового учета", "налоговые льготы", "налоговых льгот", "поддержка бизнеса",
                      "бизнес",
                      "бизнесу", "преференции", "преференций", "субсидии", "субсидия", "субсидий", "бизнеса", "стимулы",
                      "стимула",
                      "предприятия", "предприятие", "экспорт", "экспорта", "импорт", "импорта", "льгот", "займы",
                      "займов", "займа",
                      "регион", "региона", "регионов", "рыночный", "рыночного", "прогнозы", "прогнозов", "доля",
                      "долей", "анализ", "анализа",
                      "потребительское", "потребительского", "индустриальный", "индустриальные", "индустриального"]
    if any(topic in message for topic in allowed_topics):
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print(f"ChatGPT: {reply}")
        return reply

    else:
        error = QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText("Извините, это не входит в компетенцию")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()