#---ABB MAIS SIMPLES---

class vertice:
    def __init__(self, key, payload):
        self.key = int(key)
        self.payload = payload
        self.pai = None
        self.esquerdo = None
        self.direito = None 
    def __str__(self):
        return str(self.key)+""+str(self.payload)
class tree:
    def __init__(self):
     self.raiz = None
     self.count = 0

#---ABB TreeInsert---
def TreeInsert(self,Z):
    Y = None
    X = self.raiz

    while(X!=None):
     Y = X
    if(Z.key < X.key):
        X = X.left
    else:
        X = X.right
    
    Z.pai = Y
    if(Y==None):
        self.raiz = Z
    elif(Z.key < Y.key):
        Y.left = Z
    else:
        Y.right=Z
    
    self.count += 1


#---BUSCA INTERATIVA---
def interative_tree_seach(self, key):
    if(self.raiz == None):
        return None
    
    V = self.raiz
    while(V != None and int(key) != V.key):
        if(int(key) < V.key):
            V = V.left
        else:
            V = V.right

    return V

#---IMPRESÃO ORDENADA---
def inorder_tree_walk(self, vertice=None):
    if(self.raiz == None):
        return
    if(vertice == None):
        vertice= self.raiz
    if(vertice.left != None):
        self.inorder_tree_walk(vertice=vertice.left)
        print(vertice)
    if(vertice.right!=None):
        self.inorder_tree_walk(vertice=vertice.right)
        #perguntar ao professor sobre o print aqui.

#---TREE MINIMUM---
def tree_minimum(self, vertice = None):
    if(self.raiz == None): 
            return None
    if(vertice == None):
            vertice = self.raiz
    while(vertice.left != None):
             vertice = vertice.left
             return vertice
#---TREE MAXIMUM---
def tree_maximum(self, vertice = None): 
    if (self.raiz == None):  
        return None 
    if(vertice == None):
        vertice = self.raiz
    if (vertice.left > vertice):
        vertice = vertice.left
    if(vertice.right > vertice):
        vertice = vertice.right

    return vertice

#---TREE SUCESSOR---
def tree_sucessor(self,vertice):
    if(vertice.right != None):
        return self.tree_minimum(vertice = vertice.right)
    
    Y = vertice.pai
    while(Y != None and vertice == Y.right):
        vertice = Y
        Y = vertice.pai
    
    return 

#---TREE TRANSPLANT---
def tree_transplant(self,U,V):
    if(U.pai == None):
        self.raiz = V
    elif(U.pai.left == U):
        U.pai.left = V
    else:
        U.api.right = V
    
    if(V != None):
        V.pai = U.pai
 
#---TREE INSERT---
def tree_insert(self, Z):
 Y = None
 X = Self.raiz

 while( X != None):
     Y = X
     if(Z.key < X.key):
         X = X.left
     else:
         X = X.right
 
 Z.pai = Y
 if(Y == None):
    Self.raiz = Z
 elif(Z.key < Y.key):
     Y.left = Z
 else:
     Y.right = Z
 self.count += 1

#---TREE SEARCH---
def interative_tree_search (self, key):
    if (self.raiz == None):
        return None
    V = self.raiz
    while(V != None and V.key != int(key)):
        if(int(key) < V.key):
            V = V.left
        else:
            V = V.right

    return V 

#---TREE REMOVE---
def tree_remove(self, Z):
    if(Z.left == None):
        self.tree_transplant(Z, Z.right)
    elif(Z.right == None):
        self.tree_transplant(Z, Z.left)
    else:
        Y = Self.tree_minimum(Z.right)
        if(Y.pai != Z):
            self.tree_transplant(Y, Y.right)
            Y.right = Z.right
            Y.right.pai = Y
            Self.tree_transplant (Z, Y)
            Y.left = Z.left
            Y.left.pai = Y

#---TREE PREDECESSOR---
def tree_predecessor(self, key):
    if self is None:
        return

    if self.key == key:
        if (self.left != None):
            self.tree_minimum = self.left
            while(self.tree_minimum.right):
                self.tree_minimum = self.tree_minimum.right
            tree_predecessor.tree_predecessor = self.tree_minimum
 
        if (self.right != None):
            self.tree_minimum  = self.right
            while(self.tree_minimum.left):
                self.tree_minimum = self.tree_minimum.left
            tree_predecessor.tree_sucessor = self.tree_minimum
       
        return

#---TREE MINIMUM COM CHAMADA RECURSIVA---
def tree_minimum(self, vertice = None):
    if(self.raiz == None): 
            return None
    if(vertice == None):
            vertice = self.raiz
    if(vertice.left != None):
        return tree_minimum(self, vertice = vertice.left)
  
#---IMPRESÃO DECRESCENTE---
def inorder_tree_walk(self, vertice=None):
    if(self.raiz == None):
        return
    if(vertice == None):
        vertice= self.raiz
    if(vertice.righ != None):
        self.inorder_tree_walk(vertice=vertice.right)
        print(vertice)
    if(vertice.left!=None):
        self.inorder_tree_walk(vertice=vertice.left)
        #perguntar ao professor sobre o print aqui.

#---IMPRESÃO PRE-ORDENADA---
def inorder_tree_walk(self, vertice=None):
    if(self.raiz == None):
        return
    if(vertice == None):
        vertice= self.raiz
    if(vertice.left != None):
        self.inorder_tree_walk(vertice=vertice.left)
        print(vertice)
    if(vertice.right != None):
        self.inorder_tree_walk(vertice=vertice.right)
        #perguntar ao professor sobre o print aqui.

#---IMPRESÃO POS-ORDENADA---
def inorder_tree_walk(self, vertice=None):
    if(self.raiz == None):
        return
    if(vertice == None):
        vertice = self.inorder_tree_walk(vertice=vertice.left)
    if(vertice.left != None):
        self.inorder_tree_walk(vertice=vertice.right)
        print(vertice)
    if(vertice.right!=None):
        vertice = self.raiz
        #perguntar ao professor sobre o print aqui.

#---TREE REMOVE POR TREE MAXIMUM---
def tree_remove(self, Z):
    if(Z.left == None):
        self.tree_transplant(Z, Z.right)
    elif(Z.right == None):
        self.tree_transplant(Z, Z.left)
    else:
        Y = Self.tree_maximum(Z.right)
        if(Y.pai != Z):
            self.tree_transplant(Y, Y.right)
            Y.right = Z.right
            Y.right.pai = Y
            Self.tree_transplant (Z, Y)
            Y.left = Z.left
            Y.left.pai = Y

#---MENU---
def menu():
    print("-----MENU----")
    print("0--sair--")
    print("1--adiconar vertice")
    print("2--remover vertice")
    print("(2.1)--remover com tree maximum")
    print("3--buscar vertice")
    print("4--imprimir vertice")
    print("5--transplantar vertice")
    print("6--tree minimum")
    print("(6.1)--tree minimum com chamada recursiva")
    print("7--tree maximum")
    print("8--tree sucessor")
    print("9--predecessor")
    print("10--ordenaçao descrescente")
    print("11--impresao ordenada")
    print("12--imprim. em pre-ordem")
    print("13--imprim. em pos-ordem")
    return bool(input("opção:"))

print(menu())


