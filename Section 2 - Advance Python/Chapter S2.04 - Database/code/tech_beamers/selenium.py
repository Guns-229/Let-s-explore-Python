"""."""
import requests
from bs4 import BeautifulSoup
from faqs_db import Topics, Question, Choice, session


URL = "http://www.techbeamers.com/selenium-webdriver-quiz/"

resp = requests.get(URL)


soup = BeautifulSoup(resp.text, 'html.parser')

ans_selector = ".wpProQuiz_questionListItem > label > .wpProQuiz_questionInput"
topic = Topics(name="selenium")
for a in soup.select(".wpProQuiz_list")[0]:
    q = a.select(".wpProQuiz_question_text")[0].text
    quest = Question(question=q, topic=topic)
    for b in a.select(ans_selector):
        ch = Choice(choice=b.text, question=quest)
        # print(" * ", b.text)
        # ans.append(b.text)
    # print("*" * 20)
    # print(a.select(".wpProQuiz_question_text")[0].text)

    # q[a.select(".wpProQuiz_question_text")[0].text] = ans
    # quiz.append(q)

# print("*~" * 20)
# print(quiz)
