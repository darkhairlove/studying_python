#include <stdio.h>

void	ft_div_mod(int a, int b, int *div, int *mod);

int main(void)
{
	printf("ex03\n");
	
	int ex03_num1 = 20, ex03_num2 = 3;
	int div, mod;
	
	printf("num1 = %d, num2 = %d\n", ex03_num1, ex03_num2);
	
	ft_div_mod(ex03_num1, ex03_num2, &div, &mod);
	printf("div(num1, num2) = %d\nmod(num1, num2) = %d\n\n", div, mod);
}

void	ft_div_mod(int a, int b, int *div, int *mod)
{
	*div = a / b;
	*mod = a % b;
}	
