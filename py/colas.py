import queue

'''
cola = queue.Queue()

cola.put(4)
cola.put([5,6,7])

print(cola.get())#muestra el primer valor de la cola
print(cola.get())

print(cola.empty())'''


cola = queue.PriorityQueue()
cola.put(8)
cola.put(5)
cola.put(7)
cola.put(6)
cola.put(4)

print(cola.get())