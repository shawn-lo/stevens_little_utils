class Course():
    def __init__(self, course_num, course_name, prereqs,
            coreqs, coordinator, classroom, webcampus):
        self.course_num = course_num
        self.course_name = course_name
        self.prereqs = prereqs
        self.coreqs = coreqs
        self.coordinator = coordinator
        self.classroom = classroom
        self.webcampus = webcampus

    def course2dict(self):
        return{'CourseNumber':self.course_num,
                'CourseName':self.course_name,
                'Prereqs':self.prereqs,
                'Coreqs':self.coreqs,
                'Coordinator':self.coordinator,
                'Classroom':self.classroom,
                'Webcampus':self.webcampus}

    def generate_json(self):
        pass
