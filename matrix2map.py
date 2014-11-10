"""Developed using https://github.com/hachepunto/adj2cytoscape and http://stackoverflow.com/questions/17099458/python-convert-a-matrix-to-edge-list-long-form """

"""The matrix must be in a csv and the first row and collumn must include: null, (including the comma). """

"""To run it in the console. $python matrix2map.py file.csv   Will print a standard output."""

import argparse
parser = argparse.ArgumentParser(description='Convert matrix 2 csv connectivity map suitable for cytoscape and networkx.')
parser.add_argument('csv', type=argparse.FileType('r'), nargs="+", help="One or more matrices files." )
args = parser.parse_args()

for f in args.csv:
    cols = f.readline().strip().split(',')[1:]
    for line in f:
        tokens = line.strip().split(',')
        row = tokens[0]
        for column, cell in zip(cols,tokens[1:]):
            print '{},{},{}'.format(row,column,cell)
        
