def s():
  s1=int(input("ด้านที่1 = "))
  s2=int(input("ด้านที่2 = "))
  sq=s1*s2
  return(sq)
def t():
  b=int(input("ฐาน = "))
  h=int(input("สูง = "))
  tr=0.5*h*b
  return(tr)
def o():
  r=int(input("ค่า R = "))
  oo=3.14*r*r
  return(oo)




p=0
while p != 4 :

  print("______________\nmenu หาพื้นที่ \n1=สี่เหลี่ยม\n2=พื้นที่สามเหลี่ยม\n3=พื้นที่วงกลม\n4=Exit")
  p=int(input("ป้อนตัวเลข menu = "))
  if p==1:
      print("พื้นที่สี่เหลี่ยม = ",s())
  elif p==2:
    print("พื้นที่สามเหลี่ยม = ",t())
  elif p==3:
    print("พื้นที่วงกลม = ",o())
  elif p==4:
    print("Exit")
  else:
    print("no menu")

