import sys
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, backref

Base = declarative_base()

class User(Base):
	__tablename__ = "user"
	name = Column(
		String(80), nullable = False)
	email = Column(
		String(80), nullable = True)
	picture = Column(
		String(80), nullable = True)
	id = Column(
		Integer, primary_key = True)

	@property
	def serialize(self):
		#Return object data in easily serializeable format
		return {
        	'name': self.name,
        	'email': self.email,
        	'picture': self.picture,
        	'id': self.id,
    	}


class Unit(Base):
	__tablename__ = "unit"
	address = Column(
		String(180), nullable = False)
	price = Column(
		String(10), nullable=False)
	description = Column(
		String(180), nullable = False)
	user_id = Column(
		Integer, ForeignKey('user.id'))
	id = Column(
		Integer, primary_key = True)
	user = relationship(User)
	picture = Column(
		String(80), nullable = True)
	beds = Column(
		Integer, nullable=False)
	baths = Column(
		Integer, nullable=False)
	sq_feet = Column(
		Integer, nullable=True)


	@property
	def serialize(self):
		#Return object data in easily serializeable format
		return {
        	'address': self.address,
        	'description': self.description,
        	'user_id': self.user_id,
        	'id': self.id,
        	'beds': self.beds,
        	'baths': self.baths,
        	'sq_feet': self.sq_feet,
        	'picture': self.picture,
    	}
######INSERT AT END OF FILE#####

engine = create_engine('sqlite:///homehuntermanager4.db')

Base.metadata.create_all(engine)