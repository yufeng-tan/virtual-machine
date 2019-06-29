// (LL) Define data structures to represent J1 programs. 

#include <stdio.h>
#include <stdbool.h>

struct V {
	int num[100];
	bool bl[100];
	char prim[100];
};

struct E {
	struct V v; 
};

struct Prim {
	char prim[100];
};

