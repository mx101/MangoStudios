import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from data_store import DataStore

dataStore = DataStore()
majors = ["CS", "ECE", "Math", "Physics", "Chemistry", "Advertising", "English"]
years = [1, 2, 3, 4, 5]

def write_exam_histogram_image(tuples, i, major=None, year=0):
    x1 = [y for (x, y) in tuples]
    data = pd.DataFrame({"Exam " + str(i) + " Grade [%]": x1})
    fig = px.histogram(data, x="Exam " + str(i) + " Grade [%]", nbins = 20)
    if i == 0:
        data = pd.DataFrame({"Final Exam Grade [%]": x1})
        fig = px.histogram(data, x="Final Exam Grade [%]", nbins = 20)
    fig.update_xaxes(range=[20, 104])
    fig.update_yaxes()
    if i == 0:
        filename = "images/final_exam"
    else:
        filename = "images/exam" + str(i)
    if major is not None:
        filename += "_" + major
    if year != 0:
        filename += "_" + str(year)
    filename += ".png"
    fig.write_image(filename)

def write_exam_scatter_image(tuples, i, major=None, year=0):
    x = [x for (x, y) in tuples]
    y = [y for (x, y) in tuples]
    data = pd.DataFrame({"Exam " + str(i) + " Grade [%]": y, 
        "POTDs Completed": x})
    fig = px.scatter(data, x="POTDs Completed", y="Exam " + str(i) + " Grade [%]")
    if i == 0:
        data = pd.DataFrame({"Final Exam Grade [%]": y,
            "POTDs Completed": x})
        fig = px.scatter(data, x="POTDs Completed", y="Final Exam Grade [%]")
    fig.update_yaxes(range=[20, 100])
    if i == 0:
        filename = "images/final_exam" + "_potds"
    else:
        filename = "images/exam" + str(i) + "_potds"
    if major is not None:
        filename += "_" + major
    if year != 0:
        filename += "_" + str(year)
    if major is None and year == 0:
        print(len(tuples))
    filename += ".png"
    fig.write_image(filename)

def write_mp_histogram_image(tuples, i, major=None, year=0):
    x1 = [y for (x, y) in tuples]
    data = pd.DataFrame({"MP " + str(i) + " Grade [%]": x1})
    fig = px.histogram(data, x="MP " + str(i) + " Grade [%]", nbins = 20)
    fig.update_xaxes(range=[20, 104])
    filename = "images/mp" + str(i)
    if major is not None:
        filename += "_" + major
    if year != 0:
        filename += "_" + str(year)
    filename += ".png"
    fig.write_image(filename)

def write_mp_scatter_image(tuples, i, major=None, year=0):
    x = [x for (x, y) in tuples]
    y = [y for (x, y) in tuples]
    data = pd.DataFrame({"MP " + str(i) + " Grade [%]": y, 
        "First Commit [Days before due date]": x})
    fig = px.scatter(data, x="First Commit [Days before due date]", y="MP " + str(i) + " Grade [%]")
    fig.update_yaxes(range=[20, 100])
    filename = "images/mp" + str(i) + "_first_commit"
    if major is not None:
        filename += "_" + major
    if year != 0:
        filename += "_" + str(year)
    filename += ".png"
    fig.write_image(filename)

def write_mp_box_image(tuples, i, major=None, year=0):
    x = [x for (x, y) in tuples]
    # x_flipped = [x for (x, y) in tuples]
    # # Flipped No and yes on accident
    # x = []
    # for flip in x_flipped:
    #     if flip == "Yes":
    #         x.append("No")
    #     elif flip == "No":
    #         x.append("Yes")

    y = [y for (x, y) in tuples]
    data = pd.DataFrame({"MP " + str(i) + " Grade [%]": y, 
        "Number of commits": x})
    fig = px.box(data, x="Number of commits", y="MP " + str(i) + " Grade [%]")
    filename = "images/mp" + str(i) + "_number_commits"
    if major is not None:
        filename += "_" + major
    if year != 0:
        filename += "_" + str(year)
    filename += ".png"
    fig.write_image(filename)

# Generate distributions for exams

# for i in range(1,4):
#     tuples = dataStore.getXYTuples("potds", "exam" + str(i))
#     write_exam_histogram_image(tuples, i)
#     write_exam_scatter_image(tuples, i)

#     for major in majors:
#         tuples = dataStore.getXYTuples("potds", "exam" + str(i), major)
#         write_exam_histogram_image(tuples, i, major)
#     for year in years:
#         tuples = dataStore.getXYTuples("potds", "exam" + str(i), None, year)
#         write_exam_histogram_image(tuples, i, None, year)
#     for major in majors:
#         for year in years:
#             tuples = dataStore.getXYTuples("potds", "exam" + str(i), major, year)
#             write_exam_histogram_image(tuples, i, major, year)
    

    
#     for major in majors:
#         tuples = dataStore.getXYTuples("potds", "exam" + str(i), major)
#         write_exam_scatter_image(tuples, i, major)
#     for year in years:
#         tuples = dataStore.getXYTuples("potds", "exam" + str(i), None, year)
#         write_exam_scatter_image(tuples, i, None, year)
#     for major in majors:
#         for year in years:
#             tuples = dataStore.getXYTuples("potds", "exam" + str(i), major, year)
#             write_exam_scatter_image(tuples, i, major, year)


# tuples = dataStore.getXYTuples("potds", "final_exam")
# write_exam_histogram_image(tuples, 0)
# write_exam_scatter_image(tuples, 0)

# for major in majors:
#     tuples = dataStore.getXYTuples("potds", "final_exam", major)
#     write_exam_histogram_image(tuples, 0, major)
# for year in years:
#     tuples = dataStore.getXYTuples("potds", "final_exam", None, year)
#     write_exam_histogram_image(tuples, 0, None, year)
# for major in majors:
#     for year in years:
#         tuples = dataStore.getXYTuples("potds", "final_exam", major, year)
#         write_exam_histogram_image(tuples, 0, major, year)



# for major in majors:
#     tuples = dataStore.getXYTuples("potds", "final_exam", major)
#     write_exam_scatter_image(tuples, 0, major)
# for year in years:
#     tuples = dataStore.getXYTuples("potds", "final_exam", None, year)
#     write_exam_scatter_image(tuples, 0, None, year)
# for major in majors:
#     for year in years:
#         tuples = dataStore.getXYTuples("potds", "final_exam", major, year)
#         write_exam_scatter_image(tuples, 0, major, year)



# Generate distributions for MPs
# for i in range(1,7):
#     tuples = dataStore.getXYTuples("mp"+str(i)+"first_commit_time", "mp" + str(i))
#     write_mp_histogram_image(tuples, i)

#     for major in majors:
#         tuples = dataStore.getXYTuples("potds", "mp" + str(i), major)
#         write_mp_histogram_image(tuples, i, major)
#     for year in years:
#         tuples = dataStore.getXYTuples("potds", "mp" + str(i), None, year)
#         write_mp_histogram_image(tuples, i, None, year)
#     for major in majors:
#         for year in years:
#             tuples = dataStore.getXYTuples("potds", "mp" + str(i), major, year)
#             write_mp_histogram_image(tuples, i, major, year)
#     write_mp_scatter_image(tuples, i)
#     for major in majors:
#         tuples = dataStore.getXYTuples("mp"+str(i)+"first_commit_time", "mp" + str(i), major)
#         write_mp_scatter_image(tuples, i, major)
#     for year in years:
#         tuples = dataStore.getXYTuples("mp"+str(i)+"first_commit_time", "mp" + str(i), None, year)
#         write_mp_scatter_image(tuples, i, None, year)
#     for major in majors:
#         for year in years:
#             tuples = dataStore.getXYTuples("mp"+str(i)+"first_commit_time", "mp" + str(i), major, year)
#             write_mp_scatter_image(tuples, i, major, year)

# for i in range(1,7):
#     tuples = dataStore.getXYTuples("mp"+str(i)+"_extra_credit", "mp" + str(i))
#     write_mp_box_image(tuples, i)

#     for major in majors:
#         tuples = dataStore.getXYTuples("mp"+str(i)+"_extra_credit", "mp" + str(i), major)
#         write_mp_box_image(tuples, i, major)
#     for year in years:
#         tuples = dataStore.getXYTuples("mp"+str(i)+"_extra_credit", "mp" + str(i), None, year)
#         write_mp_box_image(tuples, i, None, year)
#     for major in majors:
#         for year in years:
#             tuples = dataStore.getXYTuples("mp"+str(i)+"_extra_credit", "mp" + str(i), major, year)
#             write_mp_box_image(tuples, i, major, year)
for i in range(1,7):
    tuples = dataStore.getXYTuples("mp"+str(i)+"_commits", "mp" + str(i))
    write_mp_box_image(tuples, i)

    for major in majors:
        tuples = dataStore.getXYTuples("mp"+str(i)+"_commits", "mp" + str(i), major)
        write_mp_box_image(tuples, i, major)
    for year in years:
        tuples = dataStore.getXYTuples("mp"+str(i)+"_commits", "mp" + str(i), None, year)
        write_mp_box_image(tuples, i, None, year)
    for major in majors:
        for year in years:
            tuples = dataStore.getXYTuples("mp"+str(i)+"_commits", "mp" + str(i), major, year)
            write_mp_box_image(tuples, i, major, year)


# tuples = dataStore.getXYTuples("potds", "final_grade")
# write_exam_histogram_image(tuples, 0)
# write_exam_scatter_image(tuples, 0)

# for major in majors:
#     tuples = dataStore.getXYTuples("potds", "final_grade", major)
#     write_exam_histogram_image(tuples, 0, major)
# for year in years:
#     tuples = dataStore.getXYTuples("potds", "final_grade", None, year)
#     write_exam_histogram_image(tuples, 0, None, year)
# for major in majors:
#     for year in years:
#         tuples = dataStore.getXYTuples("potds", "final_grade", major, year)
#         write_exam_histogram_image(tuples, 0, major, year)


# for major in majors:
#     tuples = dataStore.getXYTuples("potds", "final_grade", major)
#     write_exam_scatter_image(tuples, 0, major)
# for year in years:
#     tuples = dataStore.getXYTuples("potds", "final_grade", None, year)
#     write_exam_scatter_image(tuples, 0, None, year)
# for major in majors:
#     for year in years:
#         tuples = dataStore.getXYTuples("potds", "final_grade", major, year)
#         write_exam_scatter_image(tuples, 0, major, year)