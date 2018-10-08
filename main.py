import csv
from Gem import Gem
from selection_s import selection_sort_by_price
from merge_s import merge_sort_by_count_punish
from datetime import datetime


def read_data_from_file():
    data_list = []
    try:
        with open('Gem_data.csv') as csvin:
            reader = csv.reader(csvin)
            for row in reader:
                new_gem = Gem(row[0], int(row[1]), int(row[2]))
                data_list.append(new_gem)
    except FileNotFoundError:
        print("File with data does not exist")
    return data_list


def work_time(start_time, finish_time):
    return finish_time - start_time


if __name__ == "__main__":
    gem_list = read_data_from_file()
    print("Gem list:\n" + gem_list.__str__())
    start = datetime.now().microsecond
    print("\nSorted by price:\n" + selection_sort_by_price(gem_list).__str__())
    finish = datetime.now().microsecond
    print("Work time: " + work_time(start, finish).__str__())
    print("Change: " + str(Gem.change_number) + "\nCompare: " + str(Gem.comparing_number))
    Gem.reset_count()
    start = datetime.now().microsecond
    print("\nSorted by count of punish:\n" +
          merge_sort_by_count_punish(gem_list).__str__())
    finish = datetime.now().microsecond
    print("Work time: " + work_time(start, finish).__str__())
    print("Change: " + str(Gem.change_number) + "\nCompare: " + str(Gem.comparing_number))