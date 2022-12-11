from matchers import And, Or, HasAtLeast, PlaysIn, Not, HasFewerThan, All


class QueryBuilder:
    def __init__(self, query=[All()]):
        self._query = query

    def hasAtLeast(self, value, attr):
        self._query.append(HasAtLeast(value, attr))
        return QueryBuilder(self._query)

    def playsIn(self, team):
        self._query.append(PlaysIn(team))
        return QueryBuilder(self._query)

    def hasFewerThan(self, value, attr):
        self._query.append(HasFewerThan(value, attr))
        return QueryBuilder(self._query)

    def build(self):
        return And(*self._query)