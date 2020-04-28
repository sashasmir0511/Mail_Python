#include <time.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct	s_CMatrix
{
	int N;
	int M;
	int **matrix;
}				t_CMatrix;	

t_CMatrix *create_matrix()
{
	int i, j;
	int **mat;
	t_CMatrix *a;

//	randomize();
	a = (t_CMatrix*)malloc(sizeof(t_CMatrix));
	mat = (int**)malloc(sizeof(int*) * 100);
	a->N = 100;
	a->M = 100;

	i = 0;
	while (i < 100)
	{
		j = 0;
		mat[i] = (int*)malloc(sizeof(int) * 100);
		while (j < 100)
		{
			mat[i][j] = rand()%100;
			j++;
		}
		i++;
	}
	a->matrix = mat;
	return a;
}

t_CMatrix *mul_matrix(t_CMatrix *a, t_CMatrix *b)
{
	int i,j,z,s;
	int **mat;
	t_CMatrix *c;

	c = (t_CMatrix*)malloc(sizeof(t_CMatrix));
	c->N = a->M;
	c->M = b->N;
	mat = (int**)malloc(sizeof(int*) * 100);
	i = 0;
	if (a->M == b->N)
	{
		while (i < a->N)
		{
			j = 0;
			mat[i] = (int*)malloc(sizeof(int) * 100);
			while (j < b->M)
			{
				z = 0;
				s = 0;
				while (z < a->M)
				{
					s += a->matrix[i][z] * b->matrix[z][j];
					z++;
				}
				mat[i][j] = s;
				j++;
			}
			i++;
		}
		c->matrix = mat;
	}
	return c;
}

int	main(void)
{
	t_CMatrix *a;
	t_CMatrix *b;
	t_CMatrix *c;

	a = create_matrix();
	b = create_matrix();
	time_t t0 = time(0);
	c = mul_matrix(a, b);
	time_t t1 = time(0);
	double time_in_seconds = difftime(t1, t0);
	printf("N: %d, M %d\n", c->N, c->M);
	printf("Time is %f\n", time_in_seconds);
	return 0;
}