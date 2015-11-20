import urllib2
import lxml.html
from lxml import etree
from StringIO import StringIO
import json

# 1, Generate HTML file.
req = urllib2.Request('http://www.stevens.edu/ses/cs/gradcourses')
try:
	response = urllib2.urlopen(req)
except urllib2.URLError, e:
	print ("The reason is %s and the code is %s" % (e.reason, e.code))

html = response.read()
with open('./target.txt', 'w') as f:
	f.write(html)
#print html

with open('./target.txt', 'r') as f:
	broken_html = f.read()
parser = etree.HTMLParser()
tree = etree.parse(StringIO(broken_html), parser)

# 2, Find courses' information
def grad_course_xpath():
	table_exp = "//div[@class='page clearfix']/section[@id='section-content']/div[@id='zone-content']/div[@id='region-content']/table[2]//tr"
	print 'table_path: ', table_exp
	record_list = []
	for element in tree.xpath(table_exp):
		if element.tag == 'tr':
			td_list = element.getchildren()
			record = []
			for td in td_list:
				temp = td.getchildren()

				newtemp = 'none'
				if len(temp) == 0:
					newtemp = td.text
				else:
					newtemp = temp[0].text

				if(newtemp == u'\xa0'):
					newtemp = 'none'
				# add later, get ride of '\n'
				record.append(newtemp)
			#print record
		record_list.append(record)
        print record_list
	return record_list

# 3, Generate JSON
class Course(object):
	def __init__(self, course_num, course_name, prereqs,
			coreqs, coordinator, classroom, webcampus):
		self.course_num = course_num
		self.course_name = course_name
		self.prereqs = prereqs
		self.coreqs = coreqs
		self.coordinator =coordinator
		self.classroom = classroom
		self.webcampus = webcampus

def course2dict(course):
	return {
		'CourseNumber' : course.course_num,
		'CourseName' : course.course_name,
		'Prereqs' : course.prereqs,
		'Coreqs' : course.coreqs,
		'Coordinator' : course.coordinator,
		'Classroom' : course.classroom,
		'Webcampus' : course.webcampus
	}

def generate_json(l):
	pass
#	for course in l:
#		c_num = course[0]
#		c_name = course[1]
#		c_pre = course[2]
#		c_cor = course[3]
#		c_coor = course[4]
#		c_room = course[5]
#		c_web = course[6]

# test for json generating
#c = Course('1', 'Datastructure', 'none', 'none', 'Chenyue', 'Fall', 'Winter')
#print(json.dumps(c, default=course2dict))

course_list = grad_course_xpath()
with open('./information.txt', 'w') as f1:
	f1.write(str(course_list))

#generate_json(course_list)


