import sublime, sublime_plugin

class DetectIndentationEventListener(sublime_plugin.EventListener):
	def on_activated(self, view):
		if view.file_name():
			view.set_status('currentPath', view.file_name() )