#!/usr/bin/env python3
import psycopg2


# Database Connection
def db_results(query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close
    return results


# Query 3 most popular articles.
query_one = """
           select articles.title,
                  count(*) as total
           from   articles left join log
                  on log.path like concat('%', articles.slug,'%')
           group by articles.title
           order by total desc limit 3;
    """


# Query most popular authors.
query_two = """
            select authors.name,
            count(*) as total
            from articles,
                 authors,
                 log
            where articles.author = authors.id and log.path
                  like concat('%', articles.slug,'%')
            group by authors.name
            order by total desc;
    """


# Query days where the error rate is greater than 1%.
query_three = """
            select * FROM requests_error where round > 1;
    """


def question_one():
    """" Print Answer to query two"""
for title, total in db_results(query_one):
    print('Popular Article')
    print('{} ---- {} views'
          .format(title, total))
print("\n")


def question_two():
    """" Print Answer to query two"""
for author, total in db_results(query_two):
    print('TOP Author')
    print('{} --- {} views'
          .format(author, total))
print("\n")


def question_three():
    """" Print Answer to query three"""
for date, round in db_results(query_three):
    print('Days with More than one Error')
    print('{} ---- {} errors more than 1'.format(date, round))
print("\n")

if __name__ == "__main__":
    question_one()
    question_two()
    question_three()
