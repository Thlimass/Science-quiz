from sqlalchemy import inspect
from datetime import datetime

from .. import db


class Category(db.Model):
    id = db.Column(db.String(100), primary_key=True, nullable=False, unique=True)
    category_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return "<%r>" % self.category_name
