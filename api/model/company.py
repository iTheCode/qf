import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

engine = sa.create_engine("sqlite:///:memory:")
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


class CompanyModel(Base):

    __tablename__ = 'companies'

    id = sa.Column(sa.Integer, primary_key=True)
    person_id = sa.Column(sa.Integer, sa.ForeignKey('persons.id'),
                          nullable=False)
    social_name = sa.Column(sa.String(255), nullable=False)
    rut = sa.Column(sa.Integer, nullable=False)
    address = sa.Column(sa.String(255), nullable=False)
    person = relationship('PersonModel', backref=backref("companies"), uselist=False)


Base.metadata.create_all(engine)
