#/bin/python3
import os
import pandas
import random
from matplotlib import pyplot as plt

def make_plots(input_file, output_dir):
    learning_rates_dir = os.path.join(output_dir, "learning_rates")
    if not os.path.exists(learning_rates_dir):
        os.mkdir(learning_rates_dir)
    agents_dir = os.path.join(output_dir, "agents")
    if not os.path.exists(agents_dir):
        os.mkdir(agents_dir)

    df = pandas.read_csv(input_file, sep="\s*;\s*", engine='python') # Dumbass csv-parser doesn't know to trim whitespace by itself!
    df = preprocess(df)
    
    """for AP in [-1, 0, 1, 2, 3]:
        for AV in [-1, 0, 1, 2, 3]:
            plot_learning_rates(df, AP, AV)
            plt.savefig(os.path.join(learning_rates_dir, f"AP{AP}_AV{AV}.png"))
            plt.close()"""
    for R in [100, 1000, 5000, 10000, 25000]:
        plot_agents(df, R)
        plt.savefig(os.path.join(agents_dir, f"R{R}.png"))
        plt.close()

def preprocess(df):
    df["gamma"] = df["GP"]/15
    df["gamma2"] = df["GV"]/(2*15)
    df["sanity_check"] = df["gamma"] == df["gamma2"]
    if not all(df["sanity_check"]):
        raise Exception("Mismatch between GV and GP. It was not the case that 15/GP == 30/GV. (unknown row)")

    #df["1/gamma"] = 1/df["gamma"]
    return df

def plot_learning_rates(df, AP, AV):

    df = df[(df["AP"] == AP) & (df["AV"] == AV)]
    df = df.sort_values(by=['gamma'])
    fig, ax = plt.subplots()
    fig.set_figheight(8)
    fig.set_figwidth(12)

    for key, grouping in df.groupby(["R"]):
        ax = grouping.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label=f"R={key[0]}")

def plot_agents(df, R):
    fig, ax = plt.subplots()

    ax.set_yscale('log')
    fig.set_figheight(8)
    fig.set_figwidth(12)

    df = df.sort_values(by=['gamma'])

    
    df1 = df[(df["R"] == R)]
    df1 = df1[["gamma", "reward"]].groupby('gamma').min()
    print(df1) 
    ax = df1.plot(ax=ax, y="reward", ylabel="reward", label=f"MIN")

    df1 = df[(df["R"] == R)]
    df1 = df1[["gamma", "reward"]].groupby('gamma').max()
    ax = df1.plot(ax=ax, y="reward", ylabel="reward", label=f"MAX")

    df1 = df[(df["R"] == R) & (df["AP"] == 2) & (df["AV"] == 2)]
    ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label=f"Uniform")

    df1 = df[(df["R"] == R) & (df["AP"] == -1) & (df["AV"] == -1)]
    ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label=f"Lower,Lower")

    df1 = df[(df["R"] == R) & (df["AP"] == 1) & (df["AV"] == 1)]
    ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label=f"UpperUpper")
    ax.set_xlabel("1/delta")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", help="Path to csv file which stores the data.", default="~/Q-PART/experiment/BB.csv")
    parser.add_argument("--output-dir", help="Output dir.", default="~/Q-PART/experiment/BB")
    args = parser.parse_args()

    make_plots(args.input_file, args.output_dir)
