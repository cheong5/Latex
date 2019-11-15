
from graphviz import Digraph
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

s1 = Digraph('structs', filename='inheritance1', node_attr={'shape': 'record'})

s1.node('people', '{<this>people|{age | name}}')
s1.node('students', '{<this>students|{<id>age | name | stud_id}}')
s1.node('professor', '{<this>professor|{<id>age | name | pro_id}}')

s1.edges([('students:this','people:this'), ('professor:this','people:this')])

s1.view()


s2 = Digraph('structs', filename='inheritance2', node_attr={'shape': 'record'})

s2.node('people', '{<this>people|{age | name}}')
s2.node('students', '{<this>students|{<id>stud_id}}')
s2.node('professor', '{<this>professor|{<id>pro_id}}')

#s2.edges([('students:this','people:this'), ('professor:this','people:this')])

s2.view()


s3 = Digraph('structs', filename='inheritance3', node_attr={'shape': 'record'})

s3.node('people', '{<this>people|{age | name}}')
s3.node('students', '{<this>students|{<id>stud_id}}')
s3.node('professor', '{<this>professor|{<id>pro_id}}')

s3.edges([('students:this','people:this'), ('professor:this','people:this')])

s3.view()

