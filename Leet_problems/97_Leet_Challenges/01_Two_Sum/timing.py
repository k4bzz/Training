import cProfile
import pstats

from two_sum import NumList

with cProfile.Profile() as pr:
    NumList(
        [2, 11, 1, 1, 1, 1, 11, 11, 11, 111, 1, 1, 1, 1, 1, 1, 1, 1, 11,
         111, 1, 1, 1, 1, 111, 1, 1, 1, 1, 111, 1, 1, 1, 7, 3], 9).two_sum()

stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
stats.print_stats()
