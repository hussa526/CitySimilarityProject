"""
this file loads data from citydataset.csv and assigns each city a score, where demographics make up 18.75
points, population size, GDP, temperature, number of sunny days, and population density make up 10 points each,
% college educated is 8 points, number of tourists is 7 points, % of young people is 6 points, and water access,
religiousity, and crime rate are 5 points each. Added up together a city can receive a score from 0 - 89.75.
"""

import csv
import math


def csv_max_at_specified_index(csv_file: str, index: int) -> int | float:
    """
    given an index, returns the max value in that column. helper function.

    Preconditions
        - 0 < index < 16
        - csv_file == 'citydataset.csv'
    """
    max_val = 0
    with open(csv_file) as csv_f:
        reader = csv.reader(csv_f)
        next(reader)
        for row in reader:
            for i in range(0, len(row)):
                if index == i:
                    max_val = max(max_val, float(row[i]))
    return max_val


def csv_min_at_specified_index(csv_file: str, index: int) -> int | float:
    """
    given an index, returns the min value in that column. helper function for csv_crimerate_scorer and csv_religiousity_
    scorer.

    Preconditions
        -  0 < index < 16
        -  csv_file == 'citydataset.csv'

    """
    min_val = math.inf
    with open(csv_file) as csv_f:
        reader = csv.reader(csv_f)
        next(reader)
        for row in reader:
            for i in range(0, len(row)):
                if index == i:
                    min_val = min(min_val, float(row[i]))
    return min_val


def csv_demographic_scorer(csv_file: str) -> dict:

    """
    calculates an overall demographic score from the %white, %black, %hispanic, and %asian variables. The score is
    split into two categories: one that calculates how non-white a city is. The range of possible values here
    is (entirely white) 0-12 (entirely non-white). The second category evaluates how evenly split the demographics of
    a city are. The range of possible values is from 0 - 6.75. returns a dictionary where each city is a key and
    associated value is the score

    Preconditions
        -  csv_file == 'citydataset.csv'
    """
    accumulator_dict = {}
    with open(csv_file) as csv_f:
        reader = csv.reader(csv_f)
        next(reader)
        for row in reader:
            for i in range(0, len(row)):
                if i == 2:
                    even_split_score = (3 * (0.25 / (0.25 + (abs(0.25 - float(row[i])))))) + (3 * (0.25 / (0.25 + (abs(0.25 - float(row[i + 1])))))) + (3 * (0.25 / (0.25 + (abs(0.25 - float(row[i + 2])))))) + (3 * (0.25 / (0.25 + (abs(0.25 - float(row[i + 3])))))) - 5.25
                if i == 3:
                    demo_score = round((float(row[i]) + float(row[i + 1]) + float(row[i + 2])) * 12, 2)
                    accumulator_dict[row[0]] = demo_score + even_split_score
                    break
    return accumulator_dict  #a city that scores high here has both a high non-white population and is relatively
    # evenly racially split (no one overriding demographic)


def csv_pop_size_scorer(csv_file: str) -> dict:

    """
    takes the population size of a city and assigns it a score from 0-10.

    Preconditions:
         - csv_file == 'citydataset.csv'
    """
    accumulator_dict = {}
    with open(csv_file) as csv_f:
        reader = csv.reader(csv_f)
        next(reader)
        for row in reader:
            for i in range(0, len(row)):
                if i == 1:
                    accumulator_dict[row[0]] = round(
                        float(row[i]) / csv_max_at_specified_index(csv_file, 1) * 10, 2)
                    break
    return accumulator_dict


def csv_gdp_scorer(csv_file: str) -> dict:

    """
    takes the GDP of a city and assigns it a score from 0-5. cities with lower GDPs are assigned a score closer to 0,
    while those with higher GDPs receive scores closer to 5. then returns a dictionary where the key is each city and
    associated value is the score.

    Preconditions
        -  csv_file == 'citydataset.csv'
    """
    accumulator_dict = {}
    with open(csv_file) as csv_f:
        reader = csv.reader(csv_f)
        next(reader)
        for row in reader:
            for i in range(0, len(row)):
                if i == 6:
                    accumulator_dict[row[0]] = round(float(row[i]) / csv_max_at_specified_index(csv_file, 6) * 10, 2)
                    break
    return accumulator_dict


def csv_temp_scorer(csv_file: str) -> dict:

    """
    takes the temp of a city and assigns it a score from 0-10. cities with lower temperatures are assigned a score closer
    to 0, while those with higher GDPs receive scores closer to 10. then returns a dictionary where the key is each city and
    associated value is the score.

    Preconditions
        -  csv_file == 'citydataset.csv'
    """
    accumulator_dict = {}
    with open(csv_file) as csv_f:
        reader = csv.reader(csv_f)
        next(reader)
        for row in reader:
            for i in range(0, len(row)):
                if i == 7:
                    accumulator_dict[row[0]] = round(float(row[i]) / csv_max_at_specified_index('citydataset.csv', 7) * 10, 2)
                    break
    return accumulator_dict


def csv_sunny_scorer(csv_file: str) -> dict:

    """
    takes the number of sunny days of a city and assigns it a score from 0-10. cities with fewer sunny days are assigned
     a score closer to 0, while those with more sunny days receive scores closer to 10. then returns a dictionary where
     the key is each city and associated value is the score.

     Preconditions
        -  csv_file == 'citydataset.csv'

    """
    accumulator_dict = {}
    with open(csv_file) as csv_f:
        reader = csv.reader(csv_f)
        next(reader)
        for row in reader:
            for i in range(0, len(row)):
                if i == 8:
                    accumulator_dict[row[0]] = round(float(row[i]) / csv_max_at_specified_index('citydataset.csv', 8) * 10, 2)
                    break
    return accumulator_dict


def csv_young_people_scorer(csv_file: str) -> dict:
    """
    takes the % of young people of a city and assigns it a score from 0-6. cities with lower %'s are assigned a score
    closer to 0, while those with higher %'s receive scores closer to 6. then returns a dictionary where the key is each
     city and associated value is the score.

     Preconditions:
        -  csv_file == 'citydataset.csv'

    """
    accumulator_dict = {}
    with open(csv_file) as csv_f:
        reader = csv.reader(csv_f)
        next(reader)
        for row in reader:
            for i in range(0, len(row)):
                if i == 9:
                    accumulator_dict[row[0]] = round(float(row[i]) / csv_max_at_specified_index('citydataset.csv', 9) * 6, 2)
                    break
    return accumulator_dict


def csv_tourism_scorer(csv_file: str) -> dict:
    """
    takes the number of tourists of a city and assigns it a score from 0-5. cities with lower numbers are assigned a score
    closer to 0,  while those with higher numbers receive scores closer to 5. then returns a dictionary where the key is
     each city and associated value is the score.

     Preconditions
        -  csv_file == 'citydataset.csv'

    """
    accumulator_dict = {}
    with open(csv_file) as csv_f:
        reader = csv.reader(csv_f)
        next(reader)
        for row in reader:
            for i in range(0, len(row)):
                if i == 10:
                    accumulator_dict[row[0]] = round(float(row[i]) / csv_max_at_specified_index('citydataset.csv', 10) * 5, 2)
                    break
    return accumulator_dict


def csv_density_scorer(csv_file: str) -> dict:
    """
    takes the pop. density of a city and assigns it a score from 0-10. cities with lower densities are assigned a score
    closer to 0, while those with higher GDPs receive scores closer to 10. then returns a dictionary where the key is
    each city and associated value is the score.

    Preconditions
        -  csv_file == 'citydataset.csv'

    """
    accumulator_dict = {}
    with open(csv_file) as csv_f:
        reader = csv.reader(csv_f)
        next(reader)
        for row in reader:
            for i in range(0, len(row)):
                if i == 11:
                    accumulator_dict[row[0]] = round(float(row[i]) / csv_max_at_specified_index('citydataset.csv', 11) * 10, 2)
                    break
    return accumulator_dict


def csv_crimerate_scorer(csv_file: str) -> dict:
    """
    takes the crime rate per 100k people of a city and assigns it a score from 0-5. cities with higher crime rates are
    assigned a score closer to 0, while those with lower rates receive scores closer to 5. then returns a dictionary
    where the key is each city and associated value is the score.

    Preconditions
        -  csv_file == 'citydataset.csv'
    """
    accumulator_dict = {}
    with open(csv_file) as csv_f:
        reader = csv.reader(csv_f)
        next(reader)
        for row in reader:
            for i in range(0, len(row)):
                if i == 12:
                    accumulator_dict[row[0]] = round(csv_min_at_specified_index('citydataset.csv', 12) / float(row[i]) * 5, 2)
                    break
    return accumulator_dict


def csv_water_access_scorer(csv_file: str) -> dict:
    """
    reviews if a city borders on a major body of water or river and assigns it a score of either 0 or 5.
    cities located on the water are given 5, while those that aren't are given 0. then returns a dictionary
    where the key is each city and associated value is the score.

    Preconditions
    -  csv_file == 'citydataset.csv'
    """
    accumulator_dict = {}
    with open(csv_file) as csv_f:
        reader = csv.reader(csv_f)
        next(reader)
        for row in reader:
            for i in range(0, len(row)):
                if i == 13:
                    if row[i] == '1':
                        accumulator_dict[row[0]] = 5
                    else:
                        accumulator_dict[row[0]] = 0
                    break
    return accumulator_dict


def csv_college_ed_scorer(csv_file: str) -> dict:
    """
    takes the % college educated rate of a city and assigns it a score from 0-10. cities with crime rates are
    assigned a score closer to 10, while those with lower rates receive scores closer to 0. then returns a dictionary
    where the key is each city and associated value is the score.

    Preconditions
        -  csv_file == 'citydataset.csv'

    """
    accumulator_dict = {}
    with open(csv_file) as csv_f:
        reader = csv.reader(csv_f)
        next(reader)
        for row in reader:
            for i in range(0, len(row)):
                if i == 14:
                    accumulator_dict[row[0]] = round(
                        float(row[i]) / csv_max_at_specified_index('citydataset.csv', 14) * 10, 2)
                    break
    return accumulator_dict


def csv_religiousity_scorer(csv_file: str) -> dict:
    """
    takes the % no religion pop. of a city and assigns it a score from 0-5. cities with lower rates are
    assigned a score closer to 5, while those with higher rates receive scores closer to 0. then returns a dictionary
    where the key is each city and associated value is the score.

    Preconditions:
        -  csv_file == 'citydataset.csv'

    """
    accumulator_dict = {}
    with open(csv_file) as csv_f:
        reader = csv.reader(csv_f)
        next(reader)
        for row in reader:
            for i in range(0, len(row)):
                if i == 15:
                    accumulator_dict[row[0]] = round(
                        csv_min_at_specified_index('citydataset.csv', 15) / float(row[i]) * 5, 2)
                    break
    return accumulator_dict


def sort_dictionary(newdict: dict) -> dict:
    """
    takes in a dictionary and returns a new dictionary sorted in ascending fashion according to it's associated values

    >>> newdict = {'a': 1, 'b': 0, 'c': 2}
    >>> sort_dictionary(newdict)
    {'b': 0, 'a': 1, 'c': 2}

    """
    return dict(sorted(newdict.items(), key=lambda x: x[1]))


def dict_of_neighbours(inputdict: dict, differential: float) -> dict:
    """
    takes in a dictionary, and returns a new dictionary where the key is a city, and associated values are
    other cities which in turn had associated values within the differential value of the city

    >>> inputdict = {'Toronto' : 1.3, 'NewYork': 1.7, 'Spokane': 0.1, 'Buffalo': 0.8, 'Montreal': 2.1}
    >>> dict_of_neighbours(inputdict, 0.5)
    {'Toronto': ['NewYork', 'Buffalo'], 'NewYork': ['Toronto', 'Montreal'], 'Buffalo': ['Toronto'], 'Montreal': ['NewYork']}

    """

    new_dict = {}
    for ele in inputdict:
        placeholder = inputdict[ele]
        for ele2 in inputdict:
            if ele != ele2:
                if abs(placeholder - inputdict[ele2]) <= differential:
                    if ele not in new_dict:
                        new_dict[ele] = [ele2]
                    else:
                        new_dict[ele].append(ele2)
    return new_dict


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    import python_ta
    # python_ta.check_all(config={
        #'extra-imports': [],  # the names (strs) of imported modules
        #'allowed-io': [],  # the names (strs) of functions that call print/open/input
        #'max-line-length': 120
    #})
