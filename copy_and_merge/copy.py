src = open("introduction.txt", "r")
data = src.read()
src.close()

dst = open("introduction_copy.txt", "w")
dst.write(data)
dst.close()
print("File copied successfully.")