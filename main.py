import tracemalloc
import time  #библиотека для вывода времени


from View import TreeView
tracemalloc.start()
start_time = time.time()
Tree = []

with open('3.txt', 'r') as tree_file:  #Чтение из файла
  for line in tree_file:
    line = (line.strip().split(' '))
    Tree.append(line)
  print('\n', Tree, '\n')
  print("_____________________________________________\n")

stop = []
for i in range(len(Tree)):
  for j in range(len(Tree)):
    if Tree[i][0] == Tree[j][0] and i != j and not j in stop:
      print(i, '<--number of point-->', j)
      print('value of point-->', Tree[i][0])
      print("_____________________________________________\n")
      stop.append(i)  #Добавляем значение котрое мы больше не учитываем

print('\n')
TreeView(Tree)  #Функция вывода древа
print("_____________________________________________\n")
print("[%s] sec" % (time.time() - start_time))  #Вывод времени
print(tracemalloc.get_traced_memory(),'bit')
tracemalloc.stop()
