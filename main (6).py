def linearSearchProduct(productList,targetproduct):
  indices = []
  for index,product in enumerate(productList):
    if product == targetproduct:
      indices.append(index)
  return indices
product=["Shoes","Boot","Loafer", "Shoes","Sandal","Shoes"]
target= "Shoes"
target2= "apple"
result=linearSearchProduct(product,target)
print(result)