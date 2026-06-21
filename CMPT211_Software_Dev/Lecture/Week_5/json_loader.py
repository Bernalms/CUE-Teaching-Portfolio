import json
import os

# --- STEP 1: READ CSV (EXTRACT) ---
def robust_reader(filename):
    print(f"1. Extracting data from '{filename}'...")
    valid_grades = []
    try:
        with open(filename, "r") as f:
            for line in f:
                try:
                    score = int(line.strip())
                    valid_grades.append(score)
                except ValueError:
                    pass # Skip bad lines silently
    except FileNotFoundError:
        print("Error: CSV missing.")
    return valid_grades

# --- STEP 2: READ JSON (GET SETTINGS) ---
def load_settings(filename):
    print(f"2. Reading current settings from '{filename}'...")
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {} # Return empty dict if missing

# --- STEP 3: WRITE JSON (LOAD/SAVE) ---
def save_results_to_json(filename, current_settings, new_data):
    print(f"3. Saving new data to '{filename}'...")
    
    # Update the dictionary in memory
    current_settings["class_results"] = new_data
    
    # Write it back to the file
    try:
        with open(filename, "w") as f:
            # indent=4 makes it look pretty
            json.dump(current_settings, f, indent=4)
        print(" Success! Data saved to JSON.")
        
    except Exception as e:
        print(f" Error saving file: {e}")

# --- MAIN EXECUTION ---

# 1. Setup Dummy Files (So this code works for you immediately)
with open("grades.csv", "w") as f: f.write("85\n90\nN/A\n45")
with open("config.json", "w") as f: f.write('{"pass_mark": 50}')

# 2. Run the Pipeline
csv_grades = robust_reader("grades.csv")
settings = load_settings("config.json")

# 3. Save the result
save_results_to_json("config.json", settings, csv_grades)

# 4. Verify (Read it back to prove it worked)
print("\n--- Verification: Checking config.json content ---")
with open("config.json", "r") as f:
    print(f.read())