from mrjob.job import MRJob
import re
class MRImageCount(MRJob):
	def mapper(self, _, line):
		match_ext = {"png", "jpg", "gif"}
		request = re.search(r"GET ([^=]+.[a-zA-Z]{3}) HTTP",line)
		if request:
			for i in match_ext:
				if i in request.groups()[0].lower():
					yield(i, 1)
	def reducer(self, ext, occurances):
		yield(ext, sum(occurances))
if __name__ == '__main__':
	MRImageCount.run()