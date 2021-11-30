import random
import numpy as np

possible_non_tech_majors = ["Math", "Physics", "Chemistry", "Advertising", "English"]
CS_MAJOR = "CS"
ECE_MAJOR = "ECE"
NUM_STUDENTS = 2000

student_data = []

for i in range(NUM_STUDENTS):
    data_point = {}
    # Generate Major, Year of Study
    p = random.uniform(0, 1)
    if (p < 0.35):
        data_point["major"] = CS_MAJOR
    elif (p < 0.7):
        data_point["major"] = ECE_MAJOR
    else:
        p = random.randint(0, len(possible_non_tech_majors) - 1)
        data_point["major"] = possible_non_tech_majors[p]
    p = random.randint(1,5)
    data_point["year"] = p

    # Generate Lab Scores, num_commits
    for i in range(12):
        lab_key = "lab" + str(i+1)
        if (i == 0 and (data_point["major"] == CS_MAJOR or data_point["major"] == ECE_MAJOR)):
            score = random.randint(65, 100)
        elif (i == 0):
            score = random.randint(45, 100)
        else:
            last_score = data_point["lab" + str(i)]
            score = min(100, random.randint(last_score-20, last_score+20))
        if (score > 75):
            num_commits = random.randint(2,7)
        else:
            num_commits = random.randint(2,7)
        data_point[lab_key] = score
        data_point[lab_key + "_commits"] = num_commits

    # Generate MP Scores, num_commits, extra credit submission
    for i in range(6):
        mp_key = "mp" + str(i+1)
        if (i == 0 and (data_point["major"] == CS_MAJOR or data_point["major"] == ECE_MAJOR)):
            score = random.randint(65, 100)
        elif (i == 0):
            score = random.randint(45, 100)
        else:
            last_score = data_point["mp" + str(i)]
            score = min(100, random.randint(last_score-20, last_score+20))
        
        p = random.uniform(0,1)
        if (score > 75):
            num_commits = random.randint(4,11)
            if (p > 0.35):
                extra_credit = "Yes"
            else:
                extra_credit = "No"
        else:
            num_commits = random.randint(2,9)
            if (p > 0.7):
                extra_credit = "Yes"
            else:
                extra_credit = "No"

        if (score > 90):
            time_before_deadline = random.randint(5,13)
        elif (score > 75):
            time_before_deadline = random.randint(4,12)
        elif (score > 60):
            time_before_deadline = random.randint(2,11)
        else:
            time_before_deadline = random.randint(1,9)

        data_point[mp_key] = score
        data_point[mp_key + "_commits"] = num_commits
        data_point[mp_key + "_extra_credit"] = extra_credit
        data_point[mp_key + "first_commit_time"] = time_before_deadline


    # Generate Exam Scores
    for i in range(3):
        exam_key = "exam" + str(i+1)
        if (i == 0 and (data_point["major"] == CS_MAJOR or data_point["major"] == ECE_MAJOR)):
            score = random.randint(55, 100)
        elif (i == 0):
            score = random.randint(40, 100)
        else:
            last_score = data_point["exam" + str(i)]
            score = min(100, random.randint(last_score-20, last_score+20))
        data_point[exam_key] = score

    # Generate Number POTD's completed
    exam_avg = int((data_point["exam1"] + data_point["exam2"] + data_point["exam3"])/3)
    num_potds = random.randint(exam_avg - 35, exam_avg + 35)
    data_point["potds"] = num_potds

    # Generate final exam grade
    final_exam_score = min(100, random.randint(exam_avg-20, exam_avg+20))
    data_point["final_exam"] = final_exam_score

    # Compute Final Grade
    sum_scores = 0
    for i in range(12):
        sum_scores += (data_point["lab" + str(i+1)] / 100) * 10
    for i in range(6):
        sum_scores += (data_point["mp" + str(i+1)] / 100) * 60
    for i in range(3):
        sum_scores += (data_point["exam" + str(i+1)] / 100) * 100
    sum_scores += (data_point["final_exam"] / 100) * 220
    sum_scores += min(100, num_potds)
    final_grade = sum_scores/1000
    data_point["final_grade"] = int(final_grade*100)

    student_data.append(data_point)

f = open("student_data.txt", "w")
for i in range(NUM_STUDENTS):
    for k,v in student_data[i].items():
        f.write(k + ":" + str(v))
        if (k != "final_grade"):
            f.write(",")
    f.write("\n")

