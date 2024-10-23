import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime, timezone

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String(12), nullable=False)
    nombre = Column(String(150), nullable=False)
    apellido = Column(String(150), nullable=False)
    fecha_registro = Column(DateTime, default=datetime.now(timezone.utc))
    
    favoritos = relationship("Favorito")

class Personaje(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250),  nullable=False)
    especie = Column(String(250))
    genero = Column(String(250))
    nacimiento = Column(String(100))
    
    favoritos = relationship("Favorito")
    peliculas = relationship("Pelicula", secondary="personaje_pelicula")
    personaje_pelicula = relationship("PersonajePelicula")

class Pelicula(Base):
    __tablename__ = 'peliculas'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    director = Column(String)
    productor = Column(String)
    fecha_lanzamiento = Column(DateTime)
    
    personaje_pelicula = relationship("PersonajePelicula")

class PersonajePelicula(Base):
    __tablename__ = 'personaje_pelicula'
    
    id = Column(Integer, primary_key=True)
    personaje_id = Column(Integer, ForeignKey('personajes.id'), nullable=False)
    pelicula_id = Column(Integer, ForeignKey('peliculas.id'), nullable=False)
    
    personaje = relationship("Personaje")
    pelicula = relationship("Pelicula")


class Planeta(Base):
    __tablename__ = 'planetas'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    poblacion = Column(Integer)
    tipo = Column(String)
    
    favoritos = relationship("Favorito")
    planeta_pelicula = relationship("PlanetaPelicula")

class PlanetaPelicula(Base):
    __tablename__ = 'planeta_pelicula'
    
    id = Column(Integer, primary_key=True)
    planeta_id = Column(Integer, ForeignKey('planetas.id'), nullable=False)
    pelicula_id = Column(Integer, ForeignKey('peliculas.id'), nullable=False)
    planeta = relationship("Planeta")
    pelicula = relationship("Pelicula")


class Favorito(Base):
    __tablename__ = 'favoritos'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personajes.id'))
    planeta_id = Column(Integer, ForeignKey('planetas.id'))
    
    usuario = relationship("Usuario")
    personaje = relationship("Personaje")
    planeta = relationship("Planeta")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
