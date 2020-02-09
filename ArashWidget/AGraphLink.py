from ArashWidget.ALinkGUI import ALinkGUI
class AGraphLink:
    def __init__(self, link_id, start=None, end=None):
        self.link_id = link_id

        self.start = start
        self.end = end
        self.gui = ALinkGUI(link_id=link_id, start=start.gui.pos, end=end.gui.pos)
