#creation d'un emsemble vide 
ensemble_vide={}
#creation d'un ensembles avec des elements
ensemble={1,2,3,4,5}
#ajout d'un element à l'ensemble
ensemble.add(6)
# suppression d'un element de l'ensemble
ensemble.remove(3)

#verification de la presence d'un element dans l'ensemble
if 2 in ensemble:
    print("l'element2 est present dans l'element")
#parcour des elements de l'ensemble 
for element in ensemble:
    print(element)
#union de deux ensembles 
union=ensemble1.intersection(ensemble2)
# diffrenece de deux ensembles 
difference=ensemble1.difference(ensemble2)
#verification si un element est superset d'un autre
if ensemble1.issuperset(ensemble2):
    print("ensemble1 est un superset de ensemble2")
    