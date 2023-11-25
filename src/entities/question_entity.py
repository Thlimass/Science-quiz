from sqlalchemy import ForeignKey, inspect, ARRAY, String
from .category_entity import Category
from datetime import datetime
from .. import db


class Question(db.Model):
    id = db.Column(db.String(100), primary_key=True, nullable=False, unique=True)
    category_id = db.Column(ForeignKey(Category.id))
    question_text = db.Column(db.String(9999))
    correct_answer = db.Column(db.String(1000))
    answer_option = db.Column(ARRAY(String))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return "<%r>" % self.question_id
