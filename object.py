class Object:
    # anything which can be displayed on the screen: is basically just a bag of components.
    def __init__(self, x, y, blocks, graphic=None, actor=None, item=None, ai=None):
        self.x = x
        self.y = y
        self.blocks = blocks
        
        self.graphic = graphic
        if self.graphic: # let graphic component know who owns it
            self.graphic.parent = self

        self.actor = actor
        if self.actor:  # let the actor component know who owns it
            self.actor.parent = self

        self.item = item
        if self.item:
            self.item.parent = self

        self.ai = ai
        if self.ai:
            self.ai.parent = self
