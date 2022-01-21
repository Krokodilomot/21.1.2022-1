teksts=input("Ievadiet tekstu: ")
def reverseText(teksts):
  sar1 = []
  for burts in teksts:
    sar1.append(burts)
  sar1.reverse()
  teksts=""
  for elements in sar1:
    teksts+=elements
  return teksts
print(reverseText(teksts))
