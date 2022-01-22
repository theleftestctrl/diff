#include <iostream>

double parable(double x, double a, double b, double c){
return a*x*x + b*x + c;
}

double diff(double y0, double y1, double h){
return (y1 - y0)/h;
}


int main() {
	double a = 34;
	double b = 12;
	double c = 10;
	int n = 100;
	double leftborder = -2;
	double rightborder = 2;
	double h =  (rightborder - leftborder)/n;
	for (double x = leftborder; x <= rightborder; x += h){
		double y0 = parable(x, a, b, c);
		double y1 = parable(x+h, a, b, c);
		std::cout << x << "\t" << y0 << "\t"  << diff(y0, y1, h) << std::endl;
		
	}
	return 0;
}
