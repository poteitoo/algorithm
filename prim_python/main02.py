def main():
	v_new = {2}
	vertices = 5
	all_edges = {0,1,2,3,4}
	while len(v_new) != vertices:
		u = [i for i in v_new][0]
		
		iterator = [i for i in all_edges-v_new-{u}]
		for p in iterator:
			
