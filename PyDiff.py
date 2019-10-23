import difflib

first_file = "C:/Users/username/Desktop/PyDiff/Text1.txt" #Document 1
second_file = "C:/Users/username/Desktop/PyDiff/Text2.txt" #Document 2
first_file_lines = open(first_file).readlines()
second_file_lines = open(second_file).readlines()
difference = difflib.HtmlDiff().make_file(first_file_lines, second_file_lines, first_file, second_file)

difference_report = open("C:/Users/username/Desktop/PyDiff/Text1.html",'w') #Output 
difference_report.write(difference)
difference_report.close()
