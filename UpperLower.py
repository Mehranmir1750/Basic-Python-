def calcualteCase(n):

    upper = 0
    lower = 0

    for i in n:
        ascii_value = ord(i)

        if 60 <= ascii_value <= 91:
            upper +=1
        elif 97 <= ascii_value <=122:
            lower +=1

    print("Orginal String: ",n)
    print("Upper Case: ",upper)
    print("Lower Case: ",lower)

calcualteCase("My Name Is Mehran")

