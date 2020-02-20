# Description of algorithms of class Algorithms
Many realizations of algorithms were taken and supplemented 
from book of Aditya Bhargava "grokking algorithms" (Грокаем алгоритмы) 2019.


	1) dijkSearch: Dijkstra's algorithm.
		Input values (Necessary: "graph"  in format {node : {neighbour : cost of path} },
		Not necessary: "userstart" and "userfinish", otherwise algorithm find out start and finist itself.
		Output values (list of shortest way and cost pf this path).

	2) backpackAlg: algorithm of tast aboutbackpack.
		Input values (Necessary: "graph" in format {node : [weight, cost] and "lenght" -
		max weight of "backpack"}.
		Output values (maximum cost and list of things for max cost).
	
	3) setOptimization: algorithms the problem of coverage of set.
		Input values (Necessary: "need" - required coverage area and "has" available elements)
		Output values (minimum list of elements for coverage of set).
	
	4) rGraphSearch and lGraphSearch: graph search of desired item.
		Input values (Necessary: "queue" , "graph", "letter" - word of ending desired item)
		Output values (desired item)
	
	5) binarySearch: binary search.
		Input values (Necessary: "massive" of int values, "item" which need to find)
		Output values (index of desired item)
	
	6) minSearch and maxSearch: search min and max values in array.

	7) sSort: selection sort of array.
		Input values (Necessary: "massive", Not necessary: "sort" - typr of sorting
		if sort = True ->in an order of increasing, otherwise in an order of descending)
		Output values (Sorted list)

	8)fSort: fast sort of array.
		Input values (Necessary: "massive", Not necessary: "sort" - typr of sorting
		if sort = True ->in an order of increasing, otherwise in an order of descending)
		Output values (Sorted list)

	9) rFactorial and lFactorial: return factorial of input value.
	
	10) rSum and lSum: return sum of array of int values.