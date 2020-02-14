from mrjob.job import MRJob
import re
class MRImageCount(MRJob):
	def mapper(self, _, line):
		pattern = r"\[((\d{2})/([A-Z]{1}[a-z]{2})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) [+-]([\d]{4}))\][^[\]]+(\d{3}) (\d+) \"(http[s]*://[^\"]+)\""
		data = re.search(pattern, line)
		if data is not None:
			data = data.groups()
			if data[8] == "404":
				url = data[10]
				date = data[0]
				yield (date, url)

if __name__ == '__main__':
	MRImageCount.run()