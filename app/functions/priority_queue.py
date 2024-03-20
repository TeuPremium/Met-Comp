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
            raise ValueError("Prioridade precisa ser um valor numérico!")
        self._queue.append((item, priority))
        self._queue.sort(key=lambda x: x[1])

    def pop(self):
        if self.is_empty():
            raise IndexError("Tentativa de retirar elemento de uma lista vazia!")
        return self._queue.pop(0)[0]

    def is_empty(self):
        return len(self._queue) == 0
    
    def print_queue(self):
        if self.is_empty():
            print("Fila vazia!")
        else:
            print("Prioridade da Fila:")
            for item, priority in self._queue:
                print(f"Item: {item}, Prioridade: {priority}")

    def on_off_state(self):
        """Criando um lista de dicionários informando a sala e se está ligado/desligado"""
        on_off = {sala[0]: sala[3] for sala, _ in self._queue}  
        return on_off

    def get_queue(self):
        organized_queue = []
        for item, priority in self._queue:
            organized_queue.append([item, priority])
        return(organized_queue)
    
    def add_list(self, item_list, priorities):
        if len(item_list) != len(priorities):
            raise ValueError('O tamanho da lista de prioridades deve corresponder ao tamanho da lista de itens')
            
        for doc, priority in zip(item_list, priorities):
            self.push(doc, priority)
        
