from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
# artlcle表
#  create table from article(
# id int primary key autoincrement,
# title varchar(100) not null,
# content text not null,
# )

class Article(db.Model):
    __tablename__ ='article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)

db.create_all()
@app.route('/')
def index():
    # #数据增加
    # article1 = Article(title='aaa',content='bbb')
    # db.session.add(article1)
    # #事务操作
    # db.session.commit()
    #查 query专门用来查找的
    # result = Article.query.filter(Article.title == 'aaa').first()
    # print('title:%s' % result.title)
    # print('content:%s' % result.content)
    # #改
    # result = Article.query.filter(Article.title == 'aaa').first()
    # result.title = 'new title'
    # db.session.commit()
    #删
    # result = Article.query.filter(Article.content == 'bbb').first()
    # db.session.delete(result)
    # db.session.commit()

    return 'index!'


if __name__ == '__main__':
    app.run(debug=True)
