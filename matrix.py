import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def dot_product(vector_one, vector_two):
        product_sum = 0
        
        for i in range(len(vector_one)):
            product_sum += vector_one[i] * vector_two[i]
            
        return product_sum

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            determinant = int(1/self.g[0][0])
        else:
            determinant = ((self.g[0][0] * self.g[1][1]) - (self.g[0][1] * self.g[1][0]))
        
        return determinant
        

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise ValueError("Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        total = 0
        for i in range(self.h):
            for j in range(self.h):
                if i == j:
                    total += self.g[i][j]
        
        return total
        
        

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.h == 1:
            return Matrix([[1 / self.g[0][0]]])
        else:
            det = self.determinant()
            if det == 0:
                raise(ValueError, "Determinant is zero for the matrix")
            else:
                inv_g = [[1/det * self.g[1][1], 1/det * -1 * self.g[0][1]], [1/det * -1 * self.g[1][0], 1/det * self.g[0][0]]]
                    
            return Matrix(inv_g)
            
        

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose = []
        for i in range(self.w):
            row = []
            for j in range(self.h):
                row.append(self.g[j][i])
            transpose.append(row)
            
        return Matrix(transpose)
        

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        matrix_sum = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] + other[i][j])
            matrix_sum.append(row)
            
        return Matrix(matrix_sum)
        #

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        negative_values = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-1 * self[i][j])
            negative_values.append(row)
                
        return Matrix(negative_values)
                
        #

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        matrix_subtract = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] - other[i][j])
            matrix_subtract.append(row)
        
        return Matrix(matrix_subtract)
        #

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        result = []
        transpose_other = other.T()
        
        for i in range(self.h):
            row =[]
            self_row = self.g[i]
            for j in range(other.w):
                other_column = transpose_other.g[j]
                dot_pro = dot_product(self_row, other_column)
                row.append(dot_pro)
            result.append(row)
            
        return Matrix(result)
        #

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            r = []
            for i in range(self.h):
                row = self[i]
                new_row = []
                for j in range(len(row)):
                    matrix_value = self[i][j]
                    row_value = other * matrix_value
                    new_row.append(row_value)
                r.append(new_row)
            return Matrix(r)
            #