#include <stdio.h>
#include <stdlib.h>

struct Tensor
{
	double X[3]; // xx, xy, xz
	double Y[3]; // yx, yy, yz
	double Z[3]; // zx, zy, zz
};

void gridAlloc(Xlength, Ylength, Zlength)
{
	struct Tensor grid3[Xlength][Ylength][Zlength];

	for(int i = 0; i < Xlength; i++)
	{
		for(int j = 0; j < Ylength; j++)
		{
			for(int k = 0; k < Zlength; k++)
			{
				for(int n = 0; n < 3; n++)
				{
						grid3[i][j][k].X[n] = 0;
						grid3[i][j][k].Y[n] = 0;
						grid3[i][j][k].Z[n] = 0;
				}
			}
		}
	}
}

int main(int argc, char *argv[])
{
	if(argc != 0)
	{
		gridAlloc(100,100,100);
	}

	return 0;
}
