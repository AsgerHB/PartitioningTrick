#/bin/python3
import os
import pandas
import random
from pathlib import Path
from matplotlib import pyplot as plt

def make_plots(experiment, input_file, output_dir):
    learning_rates_dir = Path(output_dir, "learning_rates")
    learning_rates_dir.mkdir(parents=True, exist_ok=True)
    agents_dir = Path(output_dir, "agents")
    agents_dir.mkdir(parents=True, exist_ok=True)
    exported_to = []

    df = pandas.read_csv(input_file, sep="\s*;\s*", engine='python') # Dumbass csv-parser doesn't know to trim whitespace by itself!
    df = preprocess(df, experiment)
    
    """for AP in [-1, 0, 1, 2, 3]:
        for AV in [-1, 0, 1, 2, 3]:
            if experiment == "BB":
                plot_learning_rates_BB(df, AP, AV)
            else:
                raise Exception("Not implemented")

            plt.savefig(Path(learning_rates_dir, f"AP{AP}_AV{AV}.png"))
            plt.close()"""

    for R in df["R"].unique():
        if experiment == "BB":
            plot_agents_BB(df, R)
        elif experiment == "DC":
            plot_agents_DC(df, R)
        else:
            raise Exception("Not implemented")
        path = Path(agents_dir, f"R{R}.png")
        plt.savefig(path)
        exported_to.append(str(path))
        plt.close()
    return exported_to

def preprocess(df, experiment):
    if experiment == "BB":
        df["gamma"] = df["GP"]/15
        df["gamma2"] = df["GV"]/(2*15)
        df["sanity_check"] = df["gamma"] == df["gamma2"]
        if not all(df["sanity_check"]):
            raise Exception("Mismatch between GV and GP. It was not the case that 15/GP == 30/GV. (unknown row)")
    elif experiment == "DC": 
        df["gamma"] = df["GV"]/15
    else: 
        raise Exception("Not implemented")

    #df["1/gamma"] = 1/df["gamma"]
    return df

def plot_learning_rates_BB(df, AP, AV):

    df = df[(df["AP"] == AP) & (df["AV"] == AV)]
    df = df.sort_values(by=['gamma'])
    fig, ax = plt.subplots()
    fig.set_figheight(3)
    fig.set_figwidth(4)

    for key, grouping in df.groupby(["R"]):
        ax = grouping.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label=f"R={key[0]}")

def plot_agents_BB(df, R):
    fig, ax = plt.subplots()
    plt.ylim([0, 2000])
    #ax.set_yscale('log')
    fig.set_figheight(3)
    fig.set_figwidth(4)

    df = df.sort_values(by=['gamma'])


    # # For-loop to just print every configuration    
    """df1 = df[(df["R"] == R)]
    df1 = df1[["gamma", "reward"]].groupby('gamma').min()
    print(df1) 
    ax = df1.plot(ax=ax, y="reward", ylabel="reward", label=f"MIN")

    df1 = df[(df["R"] == R)]
    df1 = df1[["gamma", "reward"]].groupby('gamma').max()
    ax = df1.plot(ax=ax, y="reward", ylabel="reward", label=f"MAX")
    """

    df1 = df[(df["R"] == R) & (df["AP"] == 3) & (df["AV"] == 3) & (df["C"] == 2)]
    ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label=f"Memoryfull")

    df1 = df[(df["R"] == R) & (df["AP"] == -1) & (df["AV"] == -2) & (df["C"] == -1)]
    ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label="$\\alpha^{i-min}$")

    df1 = df[(df["R"] == R) & (df["AP"] == 1) & (df["AV"] == -3) & (df["C"] == 1)]
    ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label="$\\alpha^{i-max}$")

    df1 = df[(df["R"] == R) & (df["AP"] == 2) & (df["AV"] == 2) & (df["C"] == 2)]
    ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label="$\\alpha^{mean}$")

    # df1 = df[(df["R"] == R) & (df["AP"] == 2) & (df["AV"] == 2) & (df["C"] == 0)]
    # ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label=f"Uniform+Pavg")

    # df1 = df[(df["R"] == R) & (df["AP"] == -1) & (df["AV"] == -1) & (df["C"] == -1)]
    # ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label=f"Lower,Lower")

    # df1 = df[(df["R"] == R) & (df["AP"] == 1) & (df["AV"] == 1) & (df["C"] == 1)]
    # ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label=f"Upper,Upper")

    ax.set_xlabel("$i$")
    fig.tight_layout()

def plot_agents_DC(df, R):
    fig, ax = plt.subplots()
    #plt.ylim([0, 2000])
    #ax.set_yscale('log')
    fig.set_figheight(3)
    fig.set_figwidth(4)

    df = df.sort_values(by=['gamma'])


    # # For-loop to just print every configuration
    # df2 = df[(df["R"] == R)]
    # df2 = df2.groupby(["AI", "AV", "AR", "C"])
    # for (keys, group) in df2:
    #     group = group[["GV", "reward"]]
    #     group = group.sort_values(by=["GV"])
    #     label = [f"{k}{v}" for k, v in zip(["AI", "AV", "AR", "C"], keys)]
    #     label = "_".join(label)
    #     ax = group.plot(ax=ax, x="GV", y="reward", ylabel="reward", label=label)

    df1 = df[(df["R"] == R) & (df["AI"] == 3) & (df["AV"] == 3) & (df["AR"] == 3) & (df["C"] == 2)]
    ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label=f"Memoryfull") # Historical + sampled cost

    df1 = df[(df["R"] == R) & (df["AI"] == -2) & (df["AV"] == -2) & (df["AR"] == -2) & (df["C"] == -1)]
    ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label="$\\alpha^{i-min}$")

    df1 = df[(df["R"] == R) & (df["AI"] == -3) & (df["AV"] == -3) & (df["AR"] == -3) & (df["C"] == 1)]
    ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label="$\\alpha^{i-max}$")

    df1 = df[(df["R"] == R) & (df["AI"] == 2) & (df["AV"] == 2) & (df["AR"] == 2) & (df["C"] == 2)]
    ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label="$\\alpha^{mean}$")

    # df1 = df[(df["R"] == R) & (df["AI"] == 2) & (df["AV"] == 2) & (df["AR"] == 2) & (df["C"] == 0)]
    # ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label=f"Uniform+static cost")

    # df1 = df[(df["R"] == R) & (df["AI"] == -1) & (df["AV"] == -1) & (df["AR"] == -1) & (df["C"] == -1)]
    # ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label=f"Lower+worst cost")

    # df1 = df[(df["R"] == R) & (df["AI"] == 1) & (df["AV"] == 1) & (df["AR"] == 1) & (df["C"] == 1)]
    # ax = df1.plot(ax=ax, x="gamma", y="reward", ylabel="reward", label=f"Upper+best cost")

    ax.set_xlabel("$i$")
    fig.tight_layout()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment", help="E.g. BB, DC...", default="DC")
    parser.add_argument("--input-file", help="Path to csv file which stores the data.", default="experiment/DC.csv")
    parser.add_argument("--output-dir", help="Output dir.", default="experiment/DC")
    args = parser.parse_args()
    
    exported_to = make_plots(args.experiment, args.input_file, args.output_dir)
    [print(x) for x in exported_to]
    print("📈"*len(exported_to))
