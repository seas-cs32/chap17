### chap17/head.py
import sys, csv

def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: head.py input.csv')

    with open(sys.argv[1], encoding='utf-8') as fin:
        reader = csv.DictReader(fin)  # assumes file contains a header row
        for i, row in enumerate(reader):
            # Just print the first 5 rows
            if i < 5:
                print(row)
            else:
                break

if __name__ == '__main__':
    main()
