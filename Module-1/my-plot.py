import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse

def main():
    parser = argparse.ArgumentParser(description='My first stats program')
    parser.add_argument('--data1')
    parser.add_argument('--data2')

    args = parser.parse_args()

    print(f'first arg: {args.data1} \nsecond arg: {args.data2}')


if True:
    main()