import json
import csv

# pref in Json file are follow format:
# [{"location": {"like": "", "disklike": ""}}, {"time": {"like": "xx,xx,xx", "dislike": "xx"}}]


# Check if instructor has any preference
def has_pref(ins_id, ins_data):
    if ins_data[ins_id]["pref"] is not None and len(ins_data[ins_id]["pref"]) > 0:
        return True
    return False


# Match pref with current row in the csv file
def match_pref(row, ins_data, score):
    preferences = ins_data[row[1]]["pref"]
    # location
    if preferences[0]["location"]["like"] != "":
        if preferences[0]["location"]["like"] in row[2]:
            score += 1
        elif preferences[0]["location"]["dislike"] in row[2]:
            score -= 1

    time_str = row[3] + row[4]

    if preferences[1]["time"]["like"] != "":
        if time_str in preferences[1]["time"]["like"]:
            score += 1
        elif time_str in preferences[1]["time"]["dislike"]:
            score -= 1

    return score


# Ranking the time table
def score_time_table():
    score = 0
    # Load Instructors
    with open("./data files/ins_file.json", "r") as data:
        ins_data = json.load(data)

    # Load time table
    with open('timetable.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # print(ins_data["1"])
        for row in readCSV:
            if has_pref(row[1], ins_data):
                # Match preference
                score = match_pref(row, ins_data, score)

    # Output score
    print("total score is: " + str(score))


def main():
    score_time_table()


if __name__ == "__main__":
    main()
