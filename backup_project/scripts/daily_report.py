#!/usr/bin/env python3
import os
import datetime
import pandas as pd

reports_directory = "../data/reports/"
html_reports_directory = reports_directory + "html/"
json_reports_directory = reports_directory + "json/"
daily_reports_directory = reports_directory + "daily/"

def create_dataframe():
    data = {
        'FileName': [],
        'FileType': [],
        'CreationDate': [],
    }
    data = fill_dataframe(data, html_reports_directory)
    data = fill_dataframe(data, json_reports_directory)

    return pd.DataFrame(data=data)

def generate_html_report(dataframe):
    print("Generating HTML dailyreport...")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = daily_reports_directory +  "_daily-report_" + timestamp + ".html"
    
    os.makedirs(daily_reports_directory, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(dataframe.to_html())

    print(f"Report generated: {output_file}")

def fill_dataframe(data_dict, dir_path):
    try:
        if not os.path.exists(dir_path):
            print(f"Directory {dir_path} doesn't exist")
            return data_dict
        
        for entry in os.scandir(dir_path):
            if entry.is_file():
                filename = entry.name
                filename_parts = filename.split('_')
                if len(filename_parts) >= 4:
                    filetype = filename_parts[1]
                    creationdate = filename_parts[2] + '_' + filename_parts[3].split('.')[0] 
                else:
                    filetype = os.path.splitext(filename)[1][1:]
                    creationdate = datetime.datetime.fromtimestamp(entry.stat().st_mtime).strftime("%Y%m%d_%H%M%S")

                data_dict['FileName'].append(filename)
                data_dict['FileType'].append(filetype)
                data_dict['CreationDate'].append(creationdate)
            
    except Exception as e:
        print(f"Error processing directory {dir_path}: {e}")
    
    return data_dict

if __name__ == "__main__":
    df = create_dataframe()
    if not df.empty:
        generate_html_report(df)
    else:
        print("No files found to process")