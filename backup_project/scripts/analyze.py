#!/usr/bin/env python3

# Your Python code here
import datetime
import sys, os
import pandas as pd
from pandas import DataFrame

base_input_url = "../data/work/"
base_output_url = "../data/reports/"
base_json_output_url = base_output_url + "json/"
base_html_output_url = base_output_url + "html/"

def analyze_file(filename):
    try:
        print("Analyzing file...")
        if filename.endswith(".csv") :
            analyze_csv(filename)
        elif filename.endswith(".txt") :
            analyze_txt(filename)
        else:
            raise TypeError
    except TypeError:
        print("File extension not supported")

def analyze_csv(filename):
    print("Analyzing csv file...")
    df = pd.read_csv(base_input_url + filename, sep=",")
    stats = df.describe()
    generate_reports(stats, filename)

def analyze_txt(filename):
    print("Analyzing txt file...")
    with open(base_input_url + filename, "r", encoding="utf-8") as file:
        content = file.read()
        file.seek(0)
        lines = len(file.readlines())
        words = len(content.split())
        characters = len(content)
        data = {
        "metric": ["lines", "words", "characters"],
        "count": [lines, words, characters]
    }
    df = pd.DataFrame(data)

    generate_reports(df, filename)

def generate_reports(data, filename):
    print("Generating reports...")

    os.makedirs(base_json_output_url, exist_ok=True)
    os.makedirs(base_html_output_url, exist_ok=True)
    
    generate_json_report(data, filename)
    generate_html_report(data, filename)

def generate_json_report(data : DataFrame, filename):
    print("Generating JSON reports...")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = base_json_output_url + filename.split(".")[0] + "_" + timestamp + ".json"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(data.to_json(indent=2))

def generate_html_report(data : DataFrame, filename):
    print("Generating HTML reports...")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = base_html_output_url + filename.split(".")[0] + "_" + timestamp + ".html"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(data.to_html())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        analyze_file(filename)

    else:
        print("No file provided")