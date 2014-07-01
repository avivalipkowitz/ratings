import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

ENGINE = None
Session = None

Base = declarative_base()

### Class declarations go here
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable = True)
    password = Column(String(64), nullable = True)
    age = Column(Integer, nullable = True)
    zipcode = Column(String(15), nullable = True)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable = False)
    release_date = Column(DateTime, nullable = True)
    imdb_url = Column(String(64), nullable = True)

class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key = True, autoincrement = True)
    user_id = Column(Integer, nullable = False)
    movie_id = Column(Integer, nullable = False)
    rating = Column(Integer, nullable = False)



### End class declarations

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo = False)
    Session = sessionmaker(bind=ENGINE)

    return Session()



def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
