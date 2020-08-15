from app import app
from app import db

stud_identifier = db.Table('stud_ident',
    db.Column('student', db.Integer, db.ForeignKey('student.student_id')),
    db.Column('meeting', db.Integer, db.ForeignKey('meeting.meeting_id'))
    )

class Student(db.Model):
    #__tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key = True) #primary Key column, automatically generated IDs
    student_name = db.Column(db.String(80), index = True, unique = False) #name of student
    student_surname = db.Column(db.String(100), index = True, unique = False) #surname of student
    student_phone = db.Column(db.Integer, index=True, unique = True) #student phone number
    student_email = db.Column(db.String(200), index=True, unique = True) #student email
    #RELATIONSHIPS
    meetings = db.relationship('Meeting', secondary=stud_identifier, backref=db.backref('students', lazy='dynamic'))
 
    def __repr__(self):
        return "Aluno: {} {}, telefone: {}".format(self.student_name,self.student_surname,self.student_phone)

class Meeting(db.Model):
    #__tablename__='meeting'
    meeting_id = db.Column(db.Integer, primary_key =True)
    meeting_date = db.Column(db.Date, index = True, unique=False) #date of the meeting
    meeting_subject = db.Column(db.String(80), index = True, unique=False) #subject of the meeting (Aula 1, Aula 2, Aula 3)
    #RELATIONSHIPS
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.teacher_id'))
    #meeting.students.append(student) -> vai somar um aluno na tabela de identificação
    

class Teacher(db.Model):
    #__tablename__='teacher'
    teacher_id = db.Column(db.Integer, primary_key =True)
    teacher_name = db.Column(db.String(80), index = True, unique = False) #name of Teacher
    teacher_surname = db.Column(db.String(100), index = True, unique = False) #surname of teacher
    teacher_phone = db.Column(db.Integer, index=True, unique = True) #teacher phone number
    teacher_email = db.Column(db.String(200), index=True, unique = True) #Teacher email
    #RELATIONSHIPS
    meetings = db.relationship('Meeting', uselist=False, backref='teacher')

