import plateaupy  
import pprint

path = "path-to-PLATEAU/23100_nagoya-shi_2020_citygml_4_op"
pl = plateaupy.plparser(paths=[path])  
pl.loadFiles()

print(pl.bldg)
print(len(pl.bldg))
print(pl.bldg.keys())
mylist = list(pl.bldg.keys())
print(mylist) 
print(pl.bldg[mylist[0]].buildings[0].getLOD0Footprintpolygons())

# pprint.pprint(dir(pl.bldg[mylist[0]]))
# pprint.pprint(vars(pl.bldg[mylist[0]]))
