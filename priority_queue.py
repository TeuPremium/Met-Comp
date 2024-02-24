# Lista de Prioridades
'''
Indice:
push -> adiciona item à fila
pop -> remove item da fila
is_empty -> verifica se fila é vazia
print_queue -> imprime fila em ordem
get_queue -> retorna fila com prioridade
add_list -> adiciona os itens de dentro de uma lista à fila com prioridade
'''
class PriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, item, priority):
        if not isinstance(priority, (int, float)):
            raise ValueError("Priority must be a numeric value")
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
    
    def add_list(self, item_list, priorities):
        if len(item_list) != len(priorities):
            raise ValueError('Length of priorities list must match the length of item list')
            
        for doc, priority in zip(item_list, priorities):
            self.push(doc, priority)
        
