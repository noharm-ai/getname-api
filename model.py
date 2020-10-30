from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = 'paciente'
    __table_args__ = {'schema':'schema'}

    id = db.Column("cd_paciente", db.Integer, primary_key=True)
    name = db.Column('nm_paciente', db.String(250), nullable=True)