def TreeView(Tree, level=0, j=0):
  if len(Tree[j]) == 3:#если делится на 2 ветки
    TreeView(Tree, level + 1, int(Tree[j][2]))
    print(' ' * 4 * level + '-> ' + Tree[j][0])
    TreeView(Tree, level + 1, int(Tree[j][1]))
  elif len(Tree[j]) == 2:#если делится на 1 ветку
    TreeView(Tree, level + 1, int(Tree[j][1]))
    print(' ' * 4 * level + '-> ' + Tree[j][0])
  elif len(Tree[j]) == 1:#если это конечный элемент
    print(' ' * 4 * level + '-> ' + Tree[j][0])