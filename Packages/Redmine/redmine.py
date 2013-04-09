import sublime
import sublime_plugin

import webbrowser

def open_ticket(ticket_number):
    url = 'https://redmine/issues/' + ticket_number
    webbrowser.open(url) #[, new=0[, autoraise=True]]

class OpenInRedmine(sublime_plugin.WindowCommand):
    def run(self):
        def onDone(ticket_number):
            open_ticket(ticket_number)

        #print self.window.show_input_panel
        self.window.show_input_panel('Ticket Number', '', onDone, None, None)
