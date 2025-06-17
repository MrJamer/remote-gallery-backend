from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    collections = relationship("Collection", back_populates="owner")

class Collection(Base):
    __tablename__ = "collections"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="collections")
    images = relationship("Image", back_populates="collection")

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    path = Column(String)
    collection_id = Column(Integer, ForeignKey("collections.id"))
    collection = relationship("Collection", back_populates="images")
