# read and write files in python
# my_file = open("output.txt", "r+")
# "w" - write-only mode
# "r" - read-only mode
# "r+" read and write mode
# "a" - append mode, which adds any new data you write to the file to the end of the file

my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")

for x in my_list:
    my_file.write(str(x) + "\n")

my_file.close()

# just read sample
my_file = open("output.txt", "r")

print my_file.read()
my_file.close()

# another method to close file after you done operation
with open("text.txt", "w") as my_file:
    my_file.write("Done!")

# check if file was closed
with open("text.txt", "w") as my_file:
    my_file.write("Done!")
    if not my_file.closed:
        my_file.close()
    print my_file.closed
