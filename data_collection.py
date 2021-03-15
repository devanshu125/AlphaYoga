class DataCollection(object):

    def __init__(self):

        self.uid = None
        self.exe_comp = []
        self.exe_dict = {self.uid: self.exe_comp}
