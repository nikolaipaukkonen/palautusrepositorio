from matchers import And, Or, HasAtLeast, PlaysIn, Not, HasFewerThan, All

class QueryBuilder:
    def __init__(self, query=None):
        self._query = query

    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(value, attr))

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(value, attr))

    def build(self):
        return And(self._query, All())