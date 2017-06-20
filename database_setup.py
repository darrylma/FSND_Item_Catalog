from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#User class to store user information
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name' : self.name,
           'id' : self.id,
           'picture' : self.picture,
           'email' : self.email,
       }

#Team class to store name of team
class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name' : self.name,
           'id' : self.id,
       }

#Player class to store player details
class Player(Base):
    __tablename__ = 'player'

    name =Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)
    height_feet = Column(String(8))
    height_inches = Column(String(8))
    weight = Column(String(8))
    age = Column(String(8))
    position = Column(String(250))
    team_id = Column(Integer,ForeignKey('team.id'))
    team = relationship(Team)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name' : self.name,
           'id' : self.id,
           'height_feet' : self.height_feet,
           'height_inches' : self.height_inches,
           'weight' : self.weight,
           'age' : self.age,
           'position' : self.position,
       }

engine = create_engine('sqlite:///nbaplayers.db')


Base.metadata.create_all(engine)
