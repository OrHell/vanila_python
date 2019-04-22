
from pytube import YouTube

import timeit

	
def test():
	YouTube('https://www.youtube.com/watch?v=iLFTu96Gydw&list=PL_H0JmbexPEy_G7YQrepNW08mMhDg4BzD&index=3&t=0s').streams.first().download()


print(timeit.timeit("test()", setup="from __main__ import test", number=1))
