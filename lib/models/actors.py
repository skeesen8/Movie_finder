import sqlite3

CONN = sqlite3.connect('Data.db')
CURSOR = CONN.cursor()


class Actors:
    all = []

    def __init__(self, name, age, origin, oscars, id = none):
        self.name = name
        self.age = age
        self.origin = origin
        self.oscars = oscars
        self.id = id
        Actors.all.append(self)

    def all_actors(self):
        return [actor for actor in Actors.all]


    @classmethod
    def all(cls):
        sql = 'Select * FROM actors'
        list_of_tuples = cursor.execute(sql).fetchall()
        return [Actors.from_db(row) for row in list_of_tuples]

    