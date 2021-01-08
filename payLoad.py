from utilities.configurations import *


def addUser(name, job):
    body = {
        "Name": name,
        "Job": job
    }
    return body

def addBookPayload(isbn,aisle):
    body = {

        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Jen Momono"
    }
    return body

def buildPayLoadFromDB(query):
    addBody = {}
    tp = getQuery(query)  # tp stands for tuple.  getQuery method is from Configuration.getQuery(query)
    addBody['name'] = tp[0]  # The value here should be from the database
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
