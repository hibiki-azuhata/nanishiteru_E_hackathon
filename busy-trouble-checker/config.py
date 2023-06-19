
class Config:
    def __init__(self, role: int, line_id: str):
        """
        :param role: 役職 0: 先輩　1: 新人
        :param line_id:
        """
        self.role = role
        self.line_id = line_id

    def set_id(self, id: str):
        self.line_id = id

    def set_senpai(self):
        self.role = 0

    def set_shinjin(self):
        self.role = 1
