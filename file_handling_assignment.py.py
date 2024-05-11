def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, my name is Kiptoo\n")
            file.write("Here is my phone number\n")
            file.write("And here is Box number 122-20400\n")
        print("File created successfully.")
    except PermissionError:
        print("Permission denied to create the file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File creation process completed.\n")


def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            print(file.read())
    except FileNotFoundError:
        print("File not found. Please create 'my_file.txt' first.")
    except PermissionError:
        print("Permission denied to read the file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File reading process completed.\n")


def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("line 4,\n")
            file.write("Line 5 \n")
            file.write(" line 6.\n")
        print("File appended successfully.")
    except PermissionError:
        print("Permission denied to append to the file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File appending process completed.\n")


def main():
    create_file()
    read_file()
    append_file()


if __name__ == "__main__":
    main()
