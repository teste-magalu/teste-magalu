from app import db
from sqlalchemy_serializer import SerializerMixin


class Message(db.Model, SerializerMixin):
    __tablename__ = 'message'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    
    recipient = db.Column(
        db.String(40),
        unique=False,
        nullable=False
    )

    message = db.Column(
        db.String(),
        unique=False,
        nullable=False
    )

    date_time = db.Column(
        db.DateTime,
        unique=False,
        nullable=False
    )

    status = db.Column(
        db.Boolean,
        unique=False,
        nullable=False,
        default=False
    )
