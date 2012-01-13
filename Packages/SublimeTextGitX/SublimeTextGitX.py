import locale
import os
import subprocess
import sublime, sublime_plugin

class GitXCommand():
    def get_path(self):
        if self.window.active_view():
            return self.window.active_view().file_name()
        elif self.window.folders():
            return self.window.folders()[0]
        else:
            sublime.status_message(__name__ + ': No place to open GitX to')
            return False

class GitxOpenCommand(sublime_plugin.WindowCommand, GitXCommand):
    def is_enabled(self):
        return True

    def run(self, *args):
        path = self.get_path()
        if not path:
            return
        if os.path.isfile(path):
            path = os.path.dirname(path)
    
        settings = sublime.load_settings('Base File.sublime-settings')
        gitx_path = settings.get('gitx_path', '/usr/local/bin/gitx')
        
        if gitx_path in ['', None]:
            sublime.error_message(__name__ + ': gitx executable path not set')
            return False

        p = subprocess.Popen([gitx_path], cwd=path.encode(locale.getpreferredencoding(do_setlocale=True)), shell=True)

