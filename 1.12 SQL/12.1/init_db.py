from sqlalchemy import create_engine

from main import db
import models


def db_start():
    create_engine('sqlite:///tmp/test.db', convert_unicode=True)
    db.create_all()
    db.session.commit()
    post_1 = models.BlogPosts()
    post_1.subject = "Pierwszy psot"
    post_1.text = "Losowy text - post"
    db.session.add(post_1)
    db.session.commit()

if __name__ == '__main__':
    db_start()