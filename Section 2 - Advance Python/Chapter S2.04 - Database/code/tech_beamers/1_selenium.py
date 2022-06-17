"""."""
import requests
from bs4 import BeautifulSoup
from faqs_db import Topics, Question, Choice, DBSession


URL = "http://www.techbeamers.com/selenium-webdriver-quiz/"


# topics = {
#     "Selenium": {"http://www.techbeamers.com/": [
#         "latest-selenium-interview-questions-and-answers/",
#         "selenium-webdriver-interview-questions-test-engineers/",
#         "selenium-testing-interview-questions-answers/",
#         "http://www.techbeamers.com/most-asked-selenium-questions-answers/",
#         "selenium-webdriver-questions/",
#         "java-coding-questions-software-testers/"
#     ]},
#     "appium": {"http://www.techbeamers.com/": [
#         "selenium-interview-appium-questions-and-answers/"
#     ]},
#     "cucumber": {"http://www.techbeamers.com/": [
#         "selenium-webdriver-cucumber-interview-questions/"
#     ]},
#     "TestNG": {"http://www.techbeamers.com/": [
#         "testng-framework-interview-questions-answers/",
#         "selenium-testng-interview-questions-answers-part2/"
#     ]

#     }
# }

topics = {
    "Selenium": [
        "http://www.techbeamers.com/selenium-webdriver-quiz/",
        "http://www.techbeamers.com/top-30-selenium-webdriver-interview-questions/",
        "http://www.techbeamers.com/webdriver-quiz-for-selenium-interview/",
        "http://www.techbeamers.com/http://www.techbeamers.com/most-asked-selenium-questions-answers/",
        "http://www.techbeamers.com/selenium-webdriver-questions/",
        "http://www.techbeamers.com/java-coding-questions-software-testers/"
    ],
    "Python": [
        "http://www.techbeamers.com/selenium-python-quiz/"
    ],
    "Appium": [
        "http://www.techbeamers.com/selenium-webdriver-appium-quiz/"
    ],
    "TestNG": [
        "http://www.techbeamers.com/selenium-webdriver-testng-quiz-testers/",
        "http://www.techbeamers.com/selenium-testing-interview-quiz-beginners/"
    ]
}

db = DBSession()
session = db.session
for t in topics:
    topic = Topics(name=t)
    session.add(topic)
    session.flush()
    session.commit()
    for url in topics[t]:
        try:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'html.parser')
            ans_selector = ".wpProQuiz_questionListItem > label > .wpProQuiz_questionInput"

            for a in soup.select(".wpProQuiz_list")[0]:
                q = a.select(".wpProQuiz_question_text")[0].text
                quest = Question(question=q, topics=topic)
                for b in a.select(ans_selector):
                    ch = Choice(choice=b.text, question=quest)
                session.add(quest)
        except Exception as e:
            print(e)
        session.flush()
        session.commit()
