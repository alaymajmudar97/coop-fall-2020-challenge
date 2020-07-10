
class EventSourcer():
    
    
    # Do not change the signature of any functions
    
    
    def __init__(self):
        self.value = 0
        self.changes = []
        self.undo_changes=[]
    def add(self, num: int):
        self.value = self.value + num
        self.changes.append({'add':num})
        print(self.value)
    def subtract(self, num: int):
        self.value = self.value - num
        self.changes.append({'sub':num})
        print(self.value)
    def undo(self):
         if not self.changes:
            print(self.value)
        
         else:
            undo = self.changes.pop()
            self.undo_changes.append(undo)
            if 'add' in undo:
                self.subtract( undo['add'])
                self.changes.pop()
            else:
                self.add( undo['sub'])
                self.changes.pop()
            print(self.value)
        
    def redo(self):
        if not self.undo_changes:
            print(self.value)
            
        else:
            redo = self.undo_changes.pop()
            
            if 'add' in redo:
                self.add( redo['add'])
    #             self.undo_changes.pop()
            else:
                self.subtract( redo['sub'])
    #             self.undo_changes.pop()

        

    def bulk_undo(self, steps: int):
        for i in range(steps):
            self.undo()
        

    def bulk_redo(self, steps: int):
        for i in range(steps):
            self.redo()
        
        
