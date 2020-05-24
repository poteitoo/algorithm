import numpy as np


def main():
	vertices = 5
	edge_names = {'a', 'b', 'c', 'd', 'e'}
	edges = [ a:[0, 2, 0, 6, 0], 
	          b:[2, 0, 3, 8, 5], 
	          c:[0, 3, 0, 0, 7],
	          d:[6, 8, 0, 0, 9], 
	          e:[0, 5, 7, 9, 0]] 
	past = {'a'}
	part = {}
	weight = 0
	while len(past) != vertices:
		# pastに含まれる頂点
		point_in = [text for text in post][0]
		# pastに含まれない頂点
		point_out = edge_names - {point_in}
		point_out = [text for text in point_out][0]
		# mini = 0
		# point_out = edge_names - past - point_in
		# for p in point_out:
		# 	temp_mini = min(edges[p])
		# 	if temp_mini > mini:
		# 		mini = temp_mini
		
