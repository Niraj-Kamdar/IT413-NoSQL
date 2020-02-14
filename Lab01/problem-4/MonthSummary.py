from mrjob.job import MRJob
import re
class MRImageCount(MRJob):
	def mapper(self, _, line):
		pattern = r"\[(\d{2})/([A-Z]{1}[a-z]{2})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) [+-]([\d]{4})\][^[\]]+(\d{3}) (\d+) \""
		data = re.search(pattern, line)
		if data:
			data = data.groups()
			mm = data[1]
			yy = data[2]
			date = "{}-{}".format(yy, mm)
			size = data[8]
			yield (date, (1, int(size)))

	def reducer(self, month, iterator):
		requests, size = map(sum, zip(*iterator))
		yield(month, (requests, size))
if __name__ == '__main__':
	MRImageCount.run()