
class LayerManager:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)
        self.objects.sort(key=lambda o: o.layer)

    def draw(self):
        for obj in the objects:
            obj.draw()

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)
