#!/bin/python3
import os
import re
from pathlib import Path

# Add padding so every "cell" in the csv row has the same width
def add_padding(cell_width, row):
    return [(cell_width - len(c))*" " + c for c in row] 

def get_parameter_header(example_configuration):
    result = example_configuration.split("_")
    result = [re.sub(r"[0-9+-.]+", "", x) for x in result]
    return result

def read_query_results(query_results_dir, output):
    dropped_rows = 0
    # CSV header. Spacings found experimentally.
    cell_width = 8
    configurations = os.listdir(query_results_dir)
    parameter_header = get_parameter_header(configurations[0])
    results_header = ["fired", "deaths", "reward", "non-discounted"]
    header = parameter_header + results_header
    header = add_padding(cell_width, header)
    header = ";".join(header)
    print(header, file=output)
    for configuration in configurations:
        
        parameters = configuration.split("_")
        parameters = [re.sub(r"[A-Z]+", "", p) for p in parameters]
        results = get_results(query_results_dir, configuration)
        if results == None:
            dropped_rows += 1
            continue

        row = parameters + results
        row = add_padding(cell_width, row)
        row = ";".join(row)
        print(row, file=output)
    
    if dropped_rows > 0:
        print(f"Warning: Output files ignored because they were badly formed: {dropped_rows} files")
    
def get_results(base_path, folder):
    full_path = os.path.join(base_path, folder, "out")
    result = []
    if not os.path.isfile(full_path):
        return None
    with open(full_path, "r") as f:
        for line in f:
            match = re.findall(r"E\(max\) = (.+)", line)
            if len(match) == 1:
                result.append(match[0])
            elif len(match) > 1: 
                raise Exception(f"Warning: Unexpected output format. \n         Found multiple matches: {match}\n         In file: {full_path}")

    if len(result) != 4:
        print(f"Warning: Unexpected output format. Did not find the expected number of query results.\n         Found: {result}\n         In file: {full_path}")
        return None

    # Counting hard on having the right text encoding here.
    result = [re.sub(r" ± .+", "", r) for r in result] # 630.632 ± 1.14171 (95% CI) ==> 630.632
    result = [re.sub(r"≈", "", r) for r in result] # ≈ 0 ==> 0
    result = [re.sub(r"≥", "", r) for r in result]           # ≥ 0.913792 (95% CI) ==> 0.913792 (95% CI)
    result = [re.sub(r"\(95% CI\)", "", r) for r in result]  # 0.913792 (95% CI)   ==> 0.913792
    
    return result

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--query-results-dir", help="Directory of query results created by run_experiment.sh", default="raw/DC/")
    parser.add_argument("--output-file", help="Where the csv summary is saved", default="experiment/DC.csv")
    args = parser.parse_args()
    Path(os.path.dirname(args.output_file)).mkdir(parents=True, exist_ok=True)

    # print(get_results("/home/asger/BB", "AV0_AP0_GV20_GP10_R100"))
    with open(args.output_file, "w") as f:
        read_query_results(args.query_results_dir, f)
    print("😎👍")
