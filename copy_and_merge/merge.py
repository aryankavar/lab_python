with open("introduction.txt", "r") as f1,open("introduction_copy.txt", "w") as f2,open("output.txt", "w") as f3:
    f3.write(f1.read())
    f3.write("\n")
    f3.write(f1.read())
print("Files merged successfully.")