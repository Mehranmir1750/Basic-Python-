with open("myfile.txt","a") as f:
    f.write("\nThis is my first file")

with open("myfile.txt","r") as f:
    data = f.read()
    print(data)