import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse

def main():
    # parser = argparse.ArgumentParser(description='My first stats program')
    # parser.add_argument('--data1')
    # parser.add_argument('--data2')

    # args = parser.parse_args()

    # print(f'first arg: {args.data1} \nsecond arg: {args.data2}')

    crashes = sns.load_dataset("penguins")
    df = crashes.loc[range(7)] 


    # Intialize figure
    f, ax = plt.subplots()
            
    # Plot total crashes
    sns.set_color_codes("pastel")
    sns.barplot(x="bill_length_mm", y="sex", data=df,
                label="Total", color="b")

    # # Plot crashes related to speeding
    # sns.set_color_codes("muted")
    # sns.barplot(x="speeding", y="abbrev", data=df,
    #             label="Speeding-related", color="b")
    # Set title
    plt.title('Speeding-related automobile collisions', fontsize=20)

    # Set legend
    ax.legend(ncol=1, loc="lower right")
    ax.set(xlim=(0, 28), ylabel="State",
        xlabel="Automobile collisions (per billion miles)")

    # Save the image
    # plt.savefig("stacked.png")

    # Show the image
    plt.show()



if True:
    main()