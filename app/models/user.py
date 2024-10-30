# models/user.py

from flask_login import UserMixin

from ..extensions import db


class User(db.Model, UserMixin):
    """
    用户表
    """
    __tablename__ = "user"
    __table_args__ = {'comment': '用户表'}  # 给表添加注释
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="用户ID")
    username = db.Column(db.String(150), unique=True, nullable=False, comment="用户名")
    email = db.Column(db.String(150), unique=True, nullable=False, comment="用户邮箱")
    password_hash = db.Column(db.String(128), comment="用户密码")  # 储存哈希后的密码

    def __repr__(self):
        return f'<User {self.username}>'
