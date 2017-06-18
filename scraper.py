import os
import urllib
import json

def main():
    semesters = getSemesters(2)
    
    path = os.path.realpath("tex/courses/subjects/")
    for filename in os.listdir(path):
        course = filename.split('.')[0] # Just the course name
        info = getCourseData(semesters, course)
        if (len(info) > 0):
            writeCourseData(path, filename, info)

def getSemesters(number):
    url = "https://api.uqfinal.com/semesters"
    data = urllib.urlopen(url)
    dictionary = json.loads(data.read())

    semesters = []
    for semester in dictionary['data']['semesters']:
        semesters.append(semester['uqId'])

    # Limit to most recent semesters (uqfinal api doesn't do summer sem)
    semesters.sort()
    semesters.reverse()
    semesters = semesters[0:number]
    return semesters

def getCourseData(semesters, course):
    api = "https://api.uqfinal.com/course/"

    assessment = []
    print course

    for semester in semesters:
        url = api + str(semester) + "/" + course
        data = urllib.urlopen(url)
        info = json.loads(data.read())
        if info["status"] == "success":
            for item in info["data"]["assessment"]:
                assessment.append(item)
    
    return assessment

def formatAssessmentItem(item):
    task = item["taskName"]
    weight = item["weight"]
    description = "" # uqfinal api doesn't have task description

    if unicode(weight).isnumeric():
        weight = str(weight) + "\%"

    return task + " & " + weight + " & " + description + "\\\\\n" # That's 2 escaped slashes and a newline

def writeCourseData(path, coursefile, assessment):
    formatted = ""
    for item in assessment:
        formatted += formatAssessmentItem(item)

    example = "example & example\% & example \\\\" # This is the default string for an unfilled assessment section
    file = open(path + "/" + coursefile, "r+")
    contents = file.read()
    contents = contents.replace(example, formatted)
    file.seek(0)
    file.write(contents)
    file.close()

if __name__ == "__main__":
    main()