import sublime, sublime_plugin

class DetectIndentationEventListener(sublime_plugin.EventListener):
	def on_activated(self, view):
		view.set_status('currentPath', view.file_name() )