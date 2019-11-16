# The signatures of this class and its public methods are required for the automated
# grading to work. You must not change the names or the list of parameters. You may
# introduce private/protected utility methods though.


# ACHTUNG! Gibt nur 1.8 Punkte!

class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors
        self.__title = title
        self.__year = year

    def __str__(self):
        return "Publication(" + str(self.__authors).replace("'", '"') + ", " + '"' + self.__title + '"' + ", " + str(self.__year) + ")"

    def __repr__(self):
        return "Publication(" + str(self.__authors).replace("'", '"') + ", " + '"' + self.__title + '"' + ", " + str(self.__year) + ")"

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            if self.__authors == other.__authors and self.__title == other.__title and self.__year == other.__year:
                return True
            else:
                return False
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(self, other.__class__):
            if len(self.__authors) == len(other.__authors):
                if self.__authors < other.__authors:
                    return True
                else:
                    return False

            return len(self.__authors) < len(other.__authors)

        return NotImplemented

    def __le__(self, other):
        if isinstance(self, other.__class):
            if len(self.__authors) == len(other.__authors):
                if self.__authors <= other.__authors:
                    return True
                else:
                    return False
            return len(self.__authors) <= len(other.__authors)

        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(self, other.__class__):
            if len(self.__authors) == len(other.__authors):
                if self.__authors > other.__authors:
                    return True
                else:
                    return False
            return len(self.__authors) > len(other.__authors)

        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(self, other.__class__):
            if len(self.__authors) == len(other.__authors):
                if self.__authors >= other.__authors:
                    return True
                else:
                    return False
            return len(self.__authors) >= len(other.__authors)

        else:
            return NotImplemented

    def __hash__(self):
        return hash(len((self.__authors, self.__title, self.__year)))

    def copy_class(self):
        new_class = Publication(self.__authors, self.__title, self.__year)
        return new_class

    def get_authors(self):
        new = self.copy_class()
        authors_copy = new.__authors
        return authors_copy

    def get_title(self):
        new = self.copy_class()
        title_copy = new.__title
        return title_copy

    def get_year(self):
        new = self.copy_class()
        year_copy = new.__year
        return year_copy

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.


if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(s)
    print(str(p))
    assert str(p) == s

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    q1 = {}
    print(p1 == p2)  # True
    print(p2 == p3)  # False
    print(p3 == q1)
    print(p1.get_title())
    sales = {
        p1: 273,
        p2: 398,
    }


