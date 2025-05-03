import csv
from playlist_read import read
'''
Format we want:
Input: [[url1, url2, url3, url4, url5],[title1, title2, title3, title4, title5]]
a 2D list/array 

Output: csv file where column one is all titles and column 2 is all links
#a list of dictionaries

- we must clean the input into a list where each entry is
- keys that are the same will be in the same column
[{'URL': 'url1', 'TITLE': 'video1'}, {'URL': 'url2', 'TITLE': 'video2'}, {'URL': 'url3', 'TITLE': 'video3'}]
'''

def dict_to_csv_format(video_array):
    csv_format = []
    for i in range(len(video_array[0])):
        csv_format.append({"URL": video_array[0][i], "TITLE": video_array[1][i]})
    return csv_format

fields = ["TITLE", "URL"]
#test_list = [["url1", "url2", "url3", "url4", "url5"], ["video1", "video2", "video3", "video4", "video5"]]
csv_format = dict_to_csv_format(read)


with open("urls.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writerows(csv_format)

#this script for work so long as the url reads are in this format


