import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower (Base):
    __tablename__= 'Follower'
    id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer,nullable=False)
    user_from_id = Column(Integer,nullable=False)
   
    

class User (Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    firts_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email =  Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    relationship (Follower)


class Post (Base):
    __tablename__= 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(String,ForeignKey('user.id'))
    user = relationship(User)



class Comment (Base):
    __tablename__= 'Comment'
    id = Column(Integer, primary_key=True)

    comment_text = Column(String(250), nullable=False)

    post_id = Column(String,ForeignKey('post.id'))
    post = relationship(Post) 

    author_id = Column(String,ForeignKey('user.id'))
    user = relationship(User)  


class Media (Base):
    __tablename__= 'Media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

    post_id = Column(String,ForeignKey('post.id'))
    post = relationship(Post)

    

    





    




   

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
