f = open("file_handeling/one.txt", "r")
print(f.read())
f.close()

f = open("file_handeling/one.txt", "r")
print(f.readline())
f.close()

f = open("file_handeling/one.txt", "r")
print(f.readlines())
f.close()

#strip
f = open("file_handeling/one.txt", "r")
lines = f.readlines()
print(lines[1].strip())
f.close()
