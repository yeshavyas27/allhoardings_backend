from global_utilities import logging_utilities


class BaseService:
    def __init__(self):
        self.logger = logging_utilities.logger