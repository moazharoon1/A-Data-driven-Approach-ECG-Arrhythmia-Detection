import os
import scipy.io
import matplotlib.pyplot as plt
import shutil
import wfdb    #waveform
import csv

def process_file(mat_file_path, hea_file_path, result_folder, file_name):
    print("Done")
    # Read the WFDB file using rdsamp function
    signals, metadata = wfdb.rdsamp(hea_file_path)
# Access metadata information
    fs = metadata['fs']
    sig_len = metadata['sig_len']
    n_sig = metadata['n_sig']
    sig_names = metadata['sig_name']
    units = metadata['units']
    comments = metadata['comments']
    csv_file_name = os.path.join(result_folder, f"{file_name}.csv")
    with open(csv_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row to the CSV file
        header = ['time'] + sig_names
        writer.writerow(header)
        # Write the data to the CSV file
        for i in range(sig_len):
            time_stamp = i / fs  # Calculate the time stamp
            row = [time_stamp] + [signals[i][j] for j in range(n_sig)]
            writer.writerow(row)
    print(f"File {file_name} processed successfully.")
    #shutil.copy(mat_file_path, result_folder)

# Function to process a single directory
def process_directory(directory, base_dir, result_base_dir):
    result_dir = os.path.join(result_base_dir, directory)
    os.makedirs(result_dir, exist_ok=True)
    # Check if the directory contains a RECORDS file
    records_filename = 'RECORDS'
    records_dir = os.path.join(base_dir, directory.replace('/', os.sep))  # Normalize path separator
    records_file_path = os.path.join(records_dir, records_filename+'.txt')
    if os.path.exists(records_file_path):
        # Read the list of file names from the RECORDS file
        with open(records_file_path, 'r') as records_file:
            for line in records_file:
                file_name = line.strip()
                mat_file_path = os.path.join(base_dir, directory, file_name + '.mat').replace('/', os.sep)
                hea_file_path = os.path.join(base_dir, directory, file_name).replace('/', os.sep)
                # Check if both .mat and .hea files exist
                if os.path.exists(mat_file_path):
                    #Process the file
                    process_file(mat_file_path, hea_file_path, result_dir,file_name)
    # Recursively process subdirectories
    for subdir in os.listdir(records_dir):
        subdir_path = os.path.join(records_dir, subdir)
        if os.path.isdir(subdir_path):
            process_directory(subdir, base_dir, result_base_dir)

# Directory containing the first RECORDS file (which contains paths to subfolders)
records_directory = 'data'
first_records_filename = 'RECORDS.txt'
# Directory to store processed results
result_directory = 'results'
# Read the list of subfolder paths from the first RECORDS file
with open(os.path.join(records_directory, first_records_filename), 'r') as first_records_file:
    subfolder_paths = first_records_file.read().splitlines()

# Iterate over each subfolder path from the first RECORDS file
for subfolder_path in subfolder_paths:
    process_directory(subfolder_path, records_directory, result_directory)
