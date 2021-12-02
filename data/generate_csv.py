import pandas as pd
import numpy as np
from data_store import DataStore
import csv

dataStore = DataStore()
majors = ["CS", "ECE", "Math", "Physics", "Chemistry", "Advertising", "English"]
years = [1, 2, 3, 4, 5]

def write_histogram_csv(assignment, i, major=None, year=0):
    if i == -1:
        tuples = dataStore.getXYTuples("potds", assignment, major, year)
    else:
        tuples = dataStore.getXYTuples("potds", assignment + str(i), major, year)
    file_name = "csv/" + assignment + "/" + assignment
    if i >= 0:
        file_name += str(i)
    if major:
        file_name += "_" + major
    if year:
        file_name += "_" + str(year)
    file_name += ".csv"
    with open(file_name, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["score"])
        for pair in tuples:
            writer.writerow([pair[1]])

def write_scatter_csv(assignment, i, xlabel, ylabel, major=None, year=0):
    if i == -1:
        tuples = dataStore.getXYTuples(xlabel, assignment, major, year)
    else:
        tuples = dataStore.getXYTuples(xlabel, assignment + str(i), major, year)
    file_name = "csv/" + assignment + "/" + assignment
    if i >= 0:
        file_name += str(i)
    if "first_commit" not in xlabel:
        file_name += "_" + xlabel
    else:
        file_name += "_autogrades"
    if major:
        file_name += "_" + major
    if year:
        file_name += "_" + str(year)
    file_name += ".csv"
    with open(file_name, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if "first_commit" not in xlabel:
            writer.writerow([xlabel, ylabel])
        else:
            writer.writerow(["autogrades", ylabel])
        for pair in tuples:
            writer.writerow([pair[0], pair[1]])

# Exams
for i in range(1,4):
    tuples = dataStore.getXYTuples("potds", "exam" + str(i))
    with open("csv/exam/exam" + str(i) + ".csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['score'])
        for pair in tuples:
            writer.writerow([pair[1]])

    write_scatter_csv("exam", i, "potds", "score", None, 0)
    for major in majors:
        write_histogram_csv("exam", i, major, 0)
        write_scatter_csv("exam", i, "potds", "score", major, 0)
    for year in years:
        write_histogram_csv("exam", i, None, year)
        write_scatter_csv("exam", i, "potds", "score", None, year)
    for major in majors:
        for year in years:
            write_histogram_csv("exam", i, major, year)
            write_scatter_csv("exam", i, "potds", "score", major, year)

# MPs
for i in range(1,7):
    tuples = dataStore.getXYTuples("potds", "mp" + str(i))
    with open("csv/mp/mp" + str(i) + ".csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['score'])
        for pair in tuples:
            writer.writerow([pair[1]])
    
    write_scatter_csv("mp", i, "potds", "score", None, 0)
    write_scatter_csv("mp", i, "mp"+str(i)+"first_commit_time", "score", None, 0)
    for major in majors:
        write_histogram_csv("mp", i, major, 0)
        write_scatter_csv("mp", i, "potds", "score", major, 0)
        write_scatter_csv("mp", i, "mp"+str(i)+"first_commit_time", "score", major, 0)
    for year in years:
        write_histogram_csv("mp", i, None, year)
        write_scatter_csv("mp", i, "potds", "score", None, year)
        write_scatter_csv("mp", i, "mp"+str(i)+"first_commit_time", "score", None, year)
    for major in majors:
        for year in years:
            write_histogram_csv("mp", i, major, year)
            write_scatter_csv("mp", i, "potds", "score", major, year)
            write_scatter_csv("mp", i, "mp"+str(i)+"first_commit_time", "score", major, year)


# Final Grade
tuples = dataStore.getXYTuples("potds", "final_grade")
with open("csv/final_grade/final_grade" + str(i) + ".csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['score'])
    for pair in tuples:
        writer.writerow([pair[1]])

write_scatter_csv("final_grade", -1, "potds", None, 0)
for major in majors:
    write_histogram_csv("final_grade", -1, major, 0)
    write_scatter_csv("final_grade", -1, "potds", "score", major, 0)
for year in years:
    write_histogram_csv("final_grade", -1, None, year)
    write_scatter_csv("final_grade", -1, "potds", "score", None, year)
for major in majors:
    for year in years:
        write_histogram_csv("final_grade", -1, major, year)
        write_scatter_csv("final_grade", -1, "potds", "score", major, year)
