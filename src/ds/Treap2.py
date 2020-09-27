#!/usr/bin/env python3

from random import randint

class TreapNode(object):
    
    def __init__(self,key,priority):
        self.key = key
        self.priority = priority
        self.l = None
        self.r = None

class Treap(object):
    
    @staticmethod
    def gen():
        return randint(1,2**64)
    
    def __init__(self):
        self.root = None
    
    def split(self,t,key):
        if t == None:
            return (None,None)
        if key < t.key:
            l,t.l = self.split(t.l,key)
            r = t
            return (l,r)
        else:
            t.r,r = self.split(t.r,key)
            l = t
            return (l,r)
    
    def merge(self,l,r):
        if l == None:
            return r
        elif r == None:
            return l
        elif l.priority > r.priority:
            l.r = self.merge(l.r,r)
            return l
        else:
            r.l = self.merge(l,r.l)
            return r
    
    def find(self,t,key):
        if t == None:
            return False
        if t.key == key:
            return True
        elif key < t.key:
            return self.find(t.l,key)
        else:
            return self.find(t.r,key)
    
    def insert(self,key):
        novo = TreapNode(key,self.gen())
        if self.root == None:
            self.root = novo
            return
        L,R = self.split(self.root,key - 1)
        self.root = self.merge(L,novo)
        self.root = self.merge(self.root,R)
    
    def get_height(self,t):
        if t == None:
            return 0
        ans = 1
        ans = max(ans,self.get_height(t.l) + 1)
        ans = max(ans,self.get_height(t.r) + 1)
        return ans
    
    def altura(self):
        valor = self.get_height(self.root)
        return valor

alturas = []

for i in range(100):
    arvore = Treap()
    for j in range(10000):
        arvore.insert(j)
    alturas.append(arvore.altura())

print(sum(alturas)/len(alturas))