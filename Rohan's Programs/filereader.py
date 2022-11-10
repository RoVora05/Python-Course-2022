def read_and_store(filename):
    file=open(filename,"r")
    lines=file.readlines()
    for i in range(len(
        lines
        )
        ):
        lines[i]=lines[i].strip()
    print(lines)
    file.close()

def main():
    file_destination=input("Enter the file location: ")
    read_and_store(file_destination)
main()