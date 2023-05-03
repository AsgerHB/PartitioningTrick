#!/bin/python3
import os
import re

def read_query_results(query_results_dir, output):
    dropped_rows = 0
    # CSV header. Spacings found experimentally.
    print("     AV;       AP;       GV;       GP;        R;    fired;   deaths;  reward", file=output)
    configurations = os.listdir(query_results_dir)
    for configuration in configurations:
        cell_width = 7 # Min number of characters a data entry should occupy
        
        parameters = configuration.split("_")
        parameters = [re.sub(r"[A-Z]+", "", p) for p in parameters]
        
        results = get_results(query_results_dir, configuration)
        if results == None:
            dropped_rows += 1
            continue

        line = parameters + results
        line = [(cell_width - len(c))*" " + c for c in line] # Add padding so every "cell" in the csv row has the same width
        line = ";  ".join(line)
        print(line, file=output)
    
    if dropped_rows > 0:
        print(f"Warning: Output files ignored because they were badly formed: {dropped_rows} files")
    
def get_results(base_path, folder):
    full_path = os.path.join(base_path, folder, "out")
    result = []
    with open(full_path, "r") as f:
        for line in f:
            match = re.findall(r"E\(max\) = (.+)", line)
            if len(match) == 1:
                result.append(match[0])
            elif len(match) > 1: 
                raise Exception(f"Warning: Unexpected output format. \n         Found multiple matches: {match}\n         In file: {full_path}")

    if len(result) != 3:
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
    parser.add_argument("--query-results-dir", help="Directory of query results created by run_experiment.sh", default="~/Q-PART/experiment/BB")
    parser.add_argument("--output-file", help="Where the csv summary is saved", default="~/Q-PART/experiment/BB.csv")
    args = parser.parse_args()

    # print(get_results("/home/asger/BB", "AV0_AP0_GV20_GP10_R100"))
    with open(args.output_file, "w") as f:
        read_query_results(args.query_results_dir, f)
