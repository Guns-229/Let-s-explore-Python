import sqlite3 as sqlite
import json


def main(file_name):
    data = {}
    with sqlite.connect(file_name) as con:
        cur = con.cursor()
        sql = "select id, Name from Topics"
        cur.execute(sql)
        for id_topic, name in cur.execute(sql):
            cur1 = con.cursor()
            sql = "select id, question from Questions " \
                  "where topic_id=={}".format(id_topic)
            lst = []

            for id_question, question in cur1.execute(sql):
                cur2 = con.cursor()
                qst = {}
                choices = []
                # print(">  ", id_question, question)
                sql = """select c.id, c.choice, c.answer
                        from choices as c where
                        c.q_id == {}""".format(id_question)
                # print(sql)
                for idchoice, choice, answer in cur2.execute(sql):
                    chx = {}
                    chx['id'] = idchoice
                    chx['choice'] = choice
                    chx['answer'] = answer
                    choices.append(chx)
                    # print("\t\t", idchoice, choice, answer)
                qst = {
                    'id': id_question,
                    'question': question,
                    'choices': choices
                }
                lst.append(qst)
            data[name] = lst
    return data

if __name__ == "__main__":
    d = main("mayaQuest_gcp.db")
    with open('dump.json', 'w') as fp:
        json.dump(d, fp)
