# File: quadratic_polynomial_skeleton.py

class Polynomial:
    ''' To represent a quadratic polynomial, a x^2 + b x + c '''
    # TODO1: initialize the attributes
    def __init__(self, a, b, c):
        ''' To initialize the attributes '''
        # Add your code here
        self.a = a
        self.b = b
        self.c = c

    # TODO2: evaluate the polynomial for x
    def evaluate(self, x):
        ''' To evaluate the polynomial at a value '''
        # Add your code here
        return (self.a*x*x + self.b*x + self.c)
    
    def __str__(self):
        ''' To get the string representation '''
        poly_str = ""
        if self.a != 0:
            poly_str += str(self.a) + "x^2"
            if self.b != 0 or self.c != 0:
                poly_str += "+"

        if self.b != 0:
            poly_str += str(self.b) + "x"
            if self.c != 0:
                poly_str += "+"

        if self.c != 0:
            poly_str += str(self.c)

        return poly_str

    # TODO3: Return the sum of 2 polynomials 
    def __add__(self, other):
        ''' To add two polynomials '''
        # Add your code here
        return Polynomial(self.a + other.a, self.b + other.b, self.c + other.c)


if __name__ == "__main__":
    poly1 = Polynomial(3, 4, 2)
    print("The quadratic polynomial is", str(poly1))
    x = 10
    result = poly1.evaluate(x)
    print(f"Evaluate {str(poly1)} at x = {x}, the answer is {result}")

    poly2 = Polynomial(0, -4, 10)
    print("The quadratic polynomial is", str(poly2))

    print("The sum of the 2 polynomials is", str(poly1 + poly2))