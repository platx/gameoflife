import os


class ResourceManager:
    def __init__(self):
        self.resources_path = os.path.dirname(os.path.abspath(__file__)) + '/../resources/'

    def get_image_path(self, file_name):
        return self.resources_path + 'images/' + file_name
