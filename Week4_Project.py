from datetime import datetime

# Global variable to track the selected spreadsheet/conversion type
selected_spreadsheet = 1

# Inserts a comma-separated string of data into the specified CSV file path using append mode with error handling.
def insertData(file_path, data_string):
    try:
        with open(file_path, "a", newline="") as f:
            f.write(data_string + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Displays the file path being read and prints the contents of the CSV file using minimal read permissions and error handling.
def viewData(file_path):
    print(f"\n--- Reading file from path: {file_path} ---")
    try:
        with open(file_path, "r") as f:
            contents = f.read()
            if contents.strip() == "":
                print("The file is currently empty.")
            else:
                print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist yet.")
    except Exception as e:
        print(f"Error reading file: {e}")

# Converts numerical data based on the active spreadsheet formula selection.
def convertData(data):
    global selected_spreadsheet
    if selected_spreadsheet == 1:
        # F to C formula: (F - 32) * 5/9
        return (data - 32) * 5 / 9
    elif selected_spreadsheet == 2:
        # lbs to Kg formula: lbs / 2.205
        return data / 2.205
    elif selected_spreadsheet == 3:
        # in to cm formula: in * 2.54
        return data * 2.54
    else:
        return data

# Collects user input entries, calculates conversions, formats data, and stores records into ZooData.csv using insertData.
def getInput():
    try:
        num_entries = int(input("How many entries are being entered? "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    for i in range(num_entries):
        print(f"\n--- Entry {i + 1} ---")
        entry_date = input("Enter the date: ")
        
        try:
            entry_value = float(input("Enter the numerical value: "))
        except ValueError:
            print("Invalid numeric value. Skipping entry.")
            continue

        converted_value = convertData(entry_value)
        
        # Format the data into a comma-separated string
        data_record = f"{entry_date},{entry_value},{converted_value:.2f}"

        # Try-except statement to store input into ZooData.csv using insertData
        try:
            insertData("ZooData.csv", data_record)
            print(f"The following data was saved at {datetime.now()}: {data_record}.")
        except Exception as e:
            print(f"Error saving entry to CSV: {e}")

# Manages the main menu flow control, user option selections, and program routing.
def main():
    print("jorkee0238")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Input Data")
        print("2. View Current Data")
        print("3. Generate Report")
        
        choice = input("Enter your menu selection: ").strip()
        now = datetime.now()
        print(f"You chose {choice} at {now}")


        if choice == "1":
            getInput()
        elif choice == "2":
            viewData("ZooData.csv")
        else:
            print("Error: The chosen functionality is not implemented yet")


if __name__ == "__main__":
    main()
