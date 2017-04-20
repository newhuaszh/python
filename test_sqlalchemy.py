# coding=utf-8
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey

Base = declarative_base()

class User(Base):
    # 表名
    __tablename__ = 'user'
    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 数据库连接
engine = create_engine('mysql+mysqlconnector://root:zhhszhx@localhost:3306/test')
# 创建DBsession类型
DBSession = sessionmaker(bind=engine)
# 创建session对象
session = DBSession()

# # 创建新的User对象
# new_user = User(id='6', name='Sam')
# # 添加到session
# session.add(new_user)
# # 提交到数据库
# session.commit()
# # 关闭session
# session.close()

# 创建Query查询，filter是where条件，如果不写filter，则表示不过滤，返回表中全部结果
# 注意：只有当查询结果只有一个时才使用one()，如果有多个结果，使用one()会报错
#      all()返回所有行，是一个list
query_user = session.query(User).filter(User.id != '0').all()
print 'type:', type(query_user)
for user in query_user:
    print 'name:', user.name

session.close()

