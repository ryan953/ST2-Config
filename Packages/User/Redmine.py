import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # self.view.insert(edit, 0, "Hello, World!")
        url = 'https://redmine/issues/18487'
        webbrowser.open(url) #[, new=0[, autoraise=True]]
        pass
