"""
General Vector object defining properties of a vector and operations between vectors.

Written by Jacob Briones
"""

from math import acos
import string


class Vector:
    
    def __init__(self, vector, name=None):
        if name:
            self.name = name
        else:
            self.name = ''
        self.dim = len(vector)
        self.components = vector
        self.var_type = type(vector)
        self.len = sum([vector[i]*vector[i] for i in range(self.dim)])

        
    def __repr__(self):
        """Representation of Vector object as a string"""
        
        rep = 'Vector([name: {}, dim:{}, components: ['.format(self.name,self.dim)
        for i in range(self.dim):
            rep += str(self.components[i])
            if i != self.dim -1:
                rep += ', '
        rep += '] , len: {}]'.format(self.len)
        return rep

    
    def __eq__(self, other):
        """Check if two vectors are equal"""
        
        if other is None:
            return False
        
        elif other.dim != self.dim:
            return False
        
        elif other.type is not list and self.type is list:
            other_v = list(other.components)
            return self.components == other_v
        
        elif self.type is list and other.type is list:
            self_v = list(self.components)
            return self_v == other.components
        
        else:
            return None
        
    def __add__(self, other):
        """Addition of two vectors"""
        
        if other.name == '' or self.name == '':
            new_name = ''
        else:
            new_name = self.name + '+' + other.name
            
        if other.dim == self.dim:
            new = [self.components[i] + other.components[i] for i in range(self.dim)]

        else:
            raise ValueError('dimensions must match')
        return self.__class__(vector=new, name=new_name)

    
    def __mul__(self, scalar):
        """Scalar multiplication of a vector"""
        
        if not isinstance(scalar, list):
            return self.__class__(vector = [scalar*self.components[i] for i in range(self.dim)],
                                  name = self.name)

        
    def __rmul__(self, scalar):
        """Scalar Multiplication"""
        if not isinstance(scalar, list):
            return self.__class__(vector = [scalar*self.components[i] for i in range(self.dim)],
                                  name = self.name)
            
            
    def dot(self, other):
        """Dot product of two vectors"""
        
        if self.dim == other.dim and other.dim is not None:
            return sum([self.components[i]*other.components[i] for i in range(self.dim)])
        
        else:
            raise ValueError('Vectors must have same dimension')

            
    def cross(self, other, name=None):
        """Cross product of two vectors."""
        
        if name:
            new_name = name
        else:
            new_name = ''
        
        if self.dim == other.dim:
            v = []
            for i in range(self.dim):
                v.append(0)
                for j in range(self.dim):
                    if j < i or j > i:
                        for k in range(self.dim):
                            if k < i or k > i:
                                if k > j:
                                    v[i] += self.components[j]*other.components[k]
                                    
                                elif k < j:
                                    v[i] -= self.components[j]*other.components[k]
            
        else:
            raise ValueError('Dimensions must match')
            
        return self.__class__(vector=v, name=new_name)

    def angle(self, other):
        """Angle between two vectors"""
        
        if other.dim != self.dim or other is None:
            raise ValueError('Vectors must have same dimension')

        else:
            return acos(
                sum([(self.components[i]*other.components[i])for i in range(self.dim)])/(self.len*other.len))

