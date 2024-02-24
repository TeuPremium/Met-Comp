# Lista de Prioridades
'''
Indice:
push -> adiciona item à lista
pop -> remove item da lista
is_empty -> verifica se lista é vazia
print_queue -> imprime lista em ordem
get_queue -> retorna lista com prioridade
'''
class PriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, item, priority):
        self._queue.append((item, priority))
        self._queue.sort(key=lambda x: x[1])

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty list")
        return self._queue.pop(0)[0]

    def is_empty(self):
        return len(self._queue) == 0
    
    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Priority Queue:")
            for item, priority in self._queue:
                print(f"Item: {item}, Priority: {priority}")

    def get_queue(self):
        organized_queue = []
        for item, priority in self._queue:
            organized_queue.append([item, priority])
        return(organized_queue)



        