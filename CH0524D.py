wd1=['2015']
wd2=['1月','2月','3月']
wjk=[(y,m) for y in wd1 for m in wd2]
print(wjk)
mm=[]
for y in wd1:
     for m in wd2:
          mm.append((y,m))
print(mm)
wjk=["伍","晋","可"]
zs=["最","帅"]
bb=  [mm+zz for mm in wjk for zz in zs if(mm=="伍" and zz=="帅")]
print(bb)
