class Trash:
    def __init__(self, trash_type):
        self.trash_type = trash_type

class PlasticTrash(Trash):
    def __init__(self):
        super().__init__("plastic")

class PaperTrash(Trash):
    def __init__(self):
        super().__init__("paper")

class MetalTrash(Trash):
    def __init__(self):
        super().__init__("metal")

class MixedTrash(Trash):
    def __init__(self):
        super().__init__("mixed")

class BioTrash(Trash):
    def __init__(self):
        super().__init__("BIO")

class GlassTrash(Trash):
    def __init__(self):
        super().__init__("glass")
