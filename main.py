import sublime
import sublime_plugin


class CheckView(object):
	"""docstring for CheckView"""
	def __init__(self, arg):
		super(CheckView, self).__init__()
		self.arg = arg
		self.name = "checkView"
		self.__view = None


		self.__view = sublime.active_window().new_file()
		self.__view.set_name(self.name)
		self.__view.set_read_only(True)


	def getSearchPath(path):
		self.search_path = path or ""


	def getSearchFilePath():
		return ""

	
		

	def close(self):
		pass




