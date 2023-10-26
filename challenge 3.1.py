def linersearchProduct(product,targetProduct):
  indices=[]
  for index,product in enumerate(products):
    if product==targetProduct:
      indices.append(index)

  return indices


#example usage:

products=["cricket","chair","rose","wwe","mani","rose"]
target1="rose"
target2="ball"
result=linersearchProduct(products,target1)
result1=linersearchProduct(products,target2)
print(result)
print(result1)