import csv

from storages.factory import StorageFactory


def find_minimal(data=None):
    minimal = None
    for row in data:
        val = int(row[0])
        if not minimal:
            minimal = val
        elif val < minimal:
            minimal = val
    return minimal


def find_maximal(data=None):
    minimal = None
    for row in data:
        val = int(row[0])
        if not minimal:
            minimal = val
        elif val > minimal:
            minimal = val
    return minimal


def get_min_and_max(data=None, index=None):
    row = [i for i in zip(*data)][index]
    row = [float(i) for i in row]

    return min(row), max(row)


with open('../datasets/australian.dat') as f:
    reader = csv.reader(f, delimiter= ' ')

    credit_card_details = []
    for row in reader:
        credit_card_details.append(row)


results = []
indexes_to_normalize = [1, 2, 6, 9, 12, 13]
for row in credit_card_details:
    normalized_row = []
    for index, value in enumerate(row):
        if index not in indexes_to_normalize:
            continue

        _min, _max = get_min_and_max(data=credit_card_details, index=index)
        normalized = (float(value) - _min) / (_max - _min)
        normalized_row.append(normalized)

    results.append(normalized_row)


Storage = StorageFactory.factory('dat')
storage = Storage()

storage.save('australian', data=results)
