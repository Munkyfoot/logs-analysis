#!/usr/bin/env python
"""
Connection to news database.

This script provides connection to the provided news
database as well as the various methods required by 'analyze'.
"""

import psycopg2

db_name = 'news'


def get_query_results(query):
    """Passes given query to database and returns results."""
    db = psycopg2.connect(database=db_name)
    c = db.cursor()

    c.execute(query)

    results = c.fetchall()

    db.close()
    return results

def get_top_articles():
    """Query the database and return the top 3 articles."""
    query = '''
            select title, count(log.path) as views
            from articles, log
            where log.path = '/article/' || articles.slug
            group by title
            order by views desc
            limit 3;
            '''
    return get_query_results(query)


def get_top_authors():
    """Query the database and return the top authors ranked by views."""
    query = '''
            select authors.name, count(log.path) as views
            from articles, log, authors
            where articles.author = authors.id
            and log.path = '/article/' || articles.slug
            group by authors.name
            order by views desc;
            '''
    return get_query_results(query)


def get_request_errors():
    """Query the database and return the request error percentage."""
    query = '''
            select date, errorpercentage
            from (
                select t1.date, t1.requests, t2.errors,
                (cast(t2.errors as float) / cast(t1.requests as float))
                * 100.0 as errorPercentage
                from (
                    select date(time) as date, count(*) as requests
                    from log
                    group by date
                ) t1
                left join (
                    select date(time) as date, count(*) as errors
                    from log
                    where status = '404 NOT FOUND'
                    group by date
                ) t2
                on t1.date = t2.date
                order by t1.date desc
            ) data
            where data.errorPercentage > 1;
            '''
    return get_query_results(query)
