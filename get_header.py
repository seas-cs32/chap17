### chap17/get_header.py
import sys, csv

def main():
    if len(sys.argv) != 3:
        sys.exit('Usage: get_header.py input.csv output.csv')

    with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'w') as fout:
        cin = csv.reader(fin)
        cout = csv.writer(fout)

        # Read the header line
        h = next(cin)

        # Write each header label on a separate line
        for i in range(len(h)):
            cout.writerow([i, h[i]])

if __name__ == '__main__':
    main()