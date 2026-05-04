'''with open("introduction.txt", "r") as f1,open("introduction_copy.txt", "w") as f2,open("output.txt", "w") as f3:
    f3.write(f1.read())
    f3.write("\n")
    f3.write(f1.read())
print("Files merged successfully.")'''



f1 = open("abc.txt", "r")
f2 = open("xyz.txt", "r")
f3 = open("output.txt", "a")

f3.write(f1.read())
f3.write(f2.read())

f1.close()
f2.close()
f3.close()
print("Files merged successfully.")