/* Can Parlar - Prints out an employee list */

#include <stdio.h>

typedef struct employee {

	char name[25];
	char position[25];
	float salary;
} emp;
emp e1, e2, e3, e4, e5;
int output(emp e1, emp e2,emp e3, emp e4, emp e5) {
printf("%5s\t%20s%7.2f\n", e1.name, e1.position, e1.salary);
printf("%5s\t%20s%7.2f\n", e2.name, e2.position, e2.salary);
printf("%5s\t%20s%7.2f\n", e3.name, e3.position, e3.salary);
printf("%5s\t%20s%7.2f\n", e4.name, e4.position, e4.salary);
printf("%5s\t%20s%7.2f\n", e5.name, e5.position, e5.salary);
}
int main() {

struct employee e1 = {"Mike\t", "Manager\t$", 3000.50};
struct employee e2 = {"John\t", "Sales Manager\t$", 4000.70};
struct employee e3 = {"Matt\t", "Assistant Manager\t$", 2200.50};
struct employee e4 = {"Drake\t", "Accountant\t$", 1500.30};
struct employee e5 = {"Adam\t", "Manager\t$", 3400.80};
printf("Name\t\t\tPosition\tSalary\n------------------------------------------------\n");
output(e1,e2,e3,e4,e5);
	return 0; 
}
