import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email =  Column(String(250), nullable=False)
class Post (Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(String,ForeignKey('user.id'))
    user = relationship(User)
class Followers (Base):
    __tablename__= 'fallowers'
    id = Column(Integer, primary_key=True)
    number_of_followers = Column(Integer,nullable=False)
    user_id = Column(String,ForeignKey('user.id'))
    user = relationship(User)
class Follows (Base):
    __tablename__= 'fallows'
    id = Column(Integer, primary_key=True)
    number_of_follows = Column(Integer,nullable=False)

    user_id = Column(String,ForeignKey('user.id'))
    user = relationship(User)    

class Likes (Base):
    __tablename__= 'likes'
    id = Column(Integer, primary_key=True)

    post_id = Column(String,ForeignKey('post.id'))
    post = relationship(Post)

    user_id = Column(String,ForeignKey('user.id'))
    user = relationship(User)

class Comments (Base):
    __tablename__= 'comments'
    id = Column(Integer, primary_key=True)

    post_id = Column(String,ForeignKey('post.id'))
    post = relationship(Post) 

    user_id = Column(String,ForeignKey('user.id'))
    user = relationship(User)  



    




   

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
