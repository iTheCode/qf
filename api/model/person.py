import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = sa.create_engine("sqlite:///:memory:")
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


class PersonModel(Base):

    __tablename__ = 'persons'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    phone = sa.Column(sa.Integer, nullable=False)

    def __repr__(self):
        return "<Person(name={self.name!r})>".format(self=self)


Base.metadata.create_all(engine)
