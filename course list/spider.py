#! /usr/bin/env python3 -tt
import urllib.request
import lxml.html
from lxml import etree
from io import StringIO
import json

def html2etree(source):
    # get HTML
    try:
        response = urllib.request.urlopen(source)
    except urllib2.URLError as e:
        print("The reason is %s and the code is %s" % (e.reason, e.code))

    html = response.read().decode('utf-8')

    # create etree
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)
    return tree


# 2, Find courses' information
def grad_course_xpath(tree):
    table_exp = "//div[@class='page clearfix']/section[@id='section-content']/div[@id='zone-content']/div[@id='region-content']/table[2]//tr"
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
                print(,newtemp,)
				# add later, get ride of '\n'
                record.append(newtemp)
			#print record
        record_list.append(record)
    return record_list

tree = html2etree('https://www.stevens.edu/ses/cs/gradcourses')
course_list = grad_course_xpath(tree)
with open('./information.txt', 'w') as f1:
    f1.write(str(course_list))

#generate_json(course_list)


