from matchers import And, Or, HasAtLeast, PlaysIn, Not, HasFewerThan, All


class QueryBuilder:
    def __init__(self, query=All()):
        self._query = query

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._query, 
                                HasAtLeast(value, attr)))

    def playsIn(self, team):
        return QueryBuilder(And(self._query, PlaysIn(team)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._query, 
                                HasFewerThan(value, attr)))

    def oneOf(self, *query):
        return QueryBuilder(Or(*query))

    def build(self):
        return self._query