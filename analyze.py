#!/usr/bin/env python
"""
Logs analysis tool.

This program analyzes the provided news database
to find user trends.
"""

import os
from db import get_top_articles, get_top_authors, get_request_errors


def top_articles_formatted(verbose=True):
    """Retrieve the top 3 articles and format."""
    if verbose:
        print("Querying database for top 3 articles...")
    return "".join('\t"{}" - {} views\n'.format(title, views)
                   for title, views in get_top_articles())


def top_authors_formatted(verbose=True):
    """Retrieve authors (sorted by views) and format."""
    if verbose:
        print("Querying database for authors (sorted by views)...")
    return "".join('\t{} - {} views\n'.format(name, views)
                   for name, views in get_top_authors())


def request_errors_formatted(verbose=True):
    """Retrieve request error percentage and format."""
    if verbose:
        print('''Querying database for request error percentages
    greater than 1% (sorted by date)...''')
    return "".join('\t{:%b %d %Y} - {:.2f}% errors\n'
                   .format(date, errorpercentage)
                   for date, errorpercentage in get_request_errors())


def write_to_file(top_articles,
                  top_authors,
                  request_errors,
                  verbose=True):
    """Format and save analysis to file."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = '{0}/analysis.txt'.format(dir_path)
    if verbose:
        print("Saving analyis to '{0}'...".format(file_path))

    writeout = """
    News Database Analysis

    Top 3 Articles:
    {0}

    Authors (ranked by views):
    {1}

    Request Errors (over 1%):
    {2}
    """

    writeout = writeout.replace('    ', '')
    writeout = writeout.strip()

    writeout_formatted = writeout.format(top_articles,
                                         top_authors,
                                         request_errors)

    analysis_file = open(file_path, 'w')
    analysis_file.write(writeout_formatted)
    analysis_file.close()


def analyis(verbose=True, save_to_file=True):
    """Run analysis on news database."""
    # Print out the formatted string displaying the top 3 articles
    # and store in memory
    top_articles = top_articles_formatted(verbose)
    if verbose:
        print(top_articles)

    # Print out the formatted string displaying authors (sorted by views)
    # and store in memory
    top_authors = top_authors_formatted(verbose)
    if verbose:
        print(top_authors)

    # Print out the formatted string displaying error percentages
    # greater than 1% and store in memory
    request_errors = request_errors_formatted(verbose)
    if verbose:
        print(request_errors)

    if save_to_file:
        write_to_file(top_articles,
                      top_authors,
                      request_errors,
                      verbose)


if __name__ == '__main__':
    analyis()
