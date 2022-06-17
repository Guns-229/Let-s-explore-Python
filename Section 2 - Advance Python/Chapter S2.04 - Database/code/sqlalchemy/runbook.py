# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 05:52:09 2016

@author: hclqaVirtualBox1
"""

from object_test import session
import random
import string
import model


test_page = model.Page()
N = 5
test_page.title = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
test_page.content = u'Test content'
print(test_page.title)
session.add(test_page)
print("1 ----- TestPage ID")
print(test_page.id)

"""
At this point the test_page object is known to SQLAlchemy, 
but not to the database. To send it to the database, 
a flush operation can be forced:
"""

session.flush()
print("2 ----- TestPage ID")
print (test_page.id)


"""
Commits - Commits the changes in db
"""
session.commit()

""" 
Delete - To delete the test_page object from the database you would use:
"""
session.delete(test_page)
session.flush()
print("3 ----- TestPage ID")
print(test_page.id)

"""
rollback - At this point you can either commit
          the transaction or do a rollback.
          Let’s do a rollback this time:
"""
session.rollback()
print("4 ----- TestPage ID")
print(test_page.id)

"""
Query - Queries are performed with query objects that are created from the
       session. The simplest way to create and use a query object is like this:
"""
page_q = session.query(model.Page)

for page in page_q:
    print(page.title)

print("---- page_q.all()")
print(page_q.all())

page = page_q.first()
print(page.title)
print(page_q[2:5])
print(page_q.get(1).title)
#
#
#"""
#Working with Objects
#-------------------
#Now let’s think about how you could add a comment to a page. 
#    One approach would be to insert a new row in the comment table using the 
#    SQL Expression API, ensuring that the pageid field contained the value 1 
#    so that the comment was associated with the correct page via a foreign key. 
#    
#    The Object-Relational API provides a much better approach:
#"""
#
#comment1 = model.Comment()
#comment1.name= u'James'
#comment1.email = u'james@example.com'
#comment1.content = u'This page needs a bit more detail ;-)'
#comment2 = model.Comment()
#comment2.name = u'Mike'
#comment2.email = u'mike@example.com'
#page.comments.append(comment1)
#page.comments.append(comment2)
#session.commit()
