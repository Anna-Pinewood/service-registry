from itertools import cycle, islice


replicas_pool = cycle([])


def cycle_to_list(cycle_):
    return list(islice(cycle_, 10))


def next_replica():
    return next(replicas_pool)
