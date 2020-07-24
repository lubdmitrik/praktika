import os
	

	while True:
	    File_name = input("Enter file name: ")
	    mod = input("Read 1 Add data 2 rewrite 3  serch for file 4 sercg for data in file 5 else exit")
	    if mod == '1':
	        try:
	            f = open("data/"+File_name, "r")
	            print(f.read())
	        except FileNotFoundError:
	                continue
	    elif mod == '2':
	        try:
	            f = open("data/"+File_name, "w")
	            f.write(input("What to re write:"))
	        except FileNotFoundError:
	                continue
	    elif mod == '3':
	        try:
	            f = open("data/"+File_name, "a")
	            f.write(input("What to re write:"))
	        except FileNotFoundError:
	                continue
	    elif mod == '4':
	        try:
	            files = os.listdir("data/")
	            for f in files:
	                print(f)
	            f = open("data/"+File_name, "r")
	        except FileNotFoundError:
	                continue
	    elif mod == '5':
	        search = input("What are you searching for: ")
	        line_num = 0
	        try:
	            f = open("data/"+File_name, "r")
	            Lines = f.readlines()
	            for line in Lines:
	                line_num += 1
	                if search in str(line):
	                    print("there is sach data at line", line_num)
	                    break
	                else:
	                    print("There is no sach data in this file")
	                    break
	        except FileNotFoundError:
	                continue
	    else:
	       break
	    f.close()

