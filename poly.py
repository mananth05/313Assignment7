"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Mitha Ananth and Shiv Palla, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: mga2385
UT EID 2: sp56633
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    """
    Our linked list class
    """
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 3/24. If you choose to use
        # a dummy node, comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        self.dummy = Node(None, None)
        # self.head = None

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        """
        Inserts a term into our list
        """
        if coeff == 0:
            return
        cur = self.dummy.next
        prev = self.dummy
        while cur is not None:
            if cur.exp == exp:
                cur.coeff += coeff
                return
            if cur.exp < exp:
                break
            prev = cur
            cur = cur.next
        new_node = Node(coeff, exp)
        prev.next = new_node
        new_node.next = cur

    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        """
        Adds two polynomials together
        """
        res = LinkedList()
        dummy_res = res.dummy

        res_cur = dummy_res
        cur1 = self.dummy.next
        cur2 = p.dummy.next
        while cur1 is not None and cur2 is not None:
            if cur1.exp == cur2.exp:
                if cur1.coeff+cur2.coeff == 0:
                    cur1 = cur1.next
                    cur2 = cur2.next
                    continue
                res_cur.next = Node(cur1.coeff+cur2.coeff, cur1.exp)
                res_cur = res_cur.next
                cur1 = cur1.next
                cur2 = cur2.next
            elif cur1.exp < cur2.exp:
                res_cur.next = Node(cur2.coeff, cur2.exp)
                res_cur = res_cur.next
                cur2 = cur2.next
            else:
                res_cur.next = Node(cur1.coeff, cur1.exp)
                res_cur = res_cur.next
                cur1 = cur1.next
        while cur1 is not None:
            res_cur.next = Node(cur1.coeff, cur1.exp)
            res_cur = res_cur.next
            cur1 = cur1.next
        while cur2 is not None:
            res_cur.next = Node(cur2.coeff, cur2.exp)
            res_cur = res_cur.next
            cur2 = cur2.next

        return res

    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        """
        Multiplies two polynomials together
        """


    # Return a string representation of the polynomial.
    def __str__(self):
        """
        Returns the string form of the polynomial
        """
        cur = self.dummy.next
        res = []

        while cur:
            coeff = cur.coeff
            exp = cur.exp

            term = "(" + str(coeff) + ", " + str(exp) + ")"


            res.append(term)
            cur = cur.next

        if len(res) == 0:
            return ""
        return " + ".join(res)

def main():
    """
    Main method to run functional tests
    """
    # read data from stdin (terminal/file) using input() and create polynomial p

    # read data from stdin (terminal/file) using input() and create polynomial q

    # get sum of p and q as a new linked list and print sum

    # get product of p and q as a new linked list and print product


if __name__ == "__main__":
    main()
