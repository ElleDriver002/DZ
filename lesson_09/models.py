from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

    def __repr__(self):
        return (
            f"<Student(id={self.id}, "
            f"first_name='{self.first_name}', "
            f"last_name='{self.last_name}')>"
        )
