
class ShowGraph:
    def __init__(self, image_path):
        self.image_path = image_path

    def show(self):
        print("%s:show graph" % self.image_path)

    def update_iamge_path(self, new_image_path):
        self.image_path = new_image_path
