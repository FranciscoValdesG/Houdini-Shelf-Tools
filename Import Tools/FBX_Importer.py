import hou

#Root node
setRoot = hou.node("/obj")

#create tool node
mainTool = setRoot.createNode("geo", "PIPE_fbx_importer")
mainTool.setColor(hou.Color((0.18,0.31,0.62)))
mainTool.setUserData("nodeshape", "circle")


#create importer

importer = mainTool.createNode("file","Input")
importer.moveToGoodPosition()

#create transform

transform = mainTool.createNode("xform", "scale")
transform.setInput(0,importer)
scale = hou.parm("/obj/PIPE_fbx_importer/scale/scale")
scale.set(1)

#create attribute delete
attdel = mainTool.createNode("attribdelete", "Del_Attributes")
attdel.setInput(0,transform)
delCd = hou.parm("/obj/PIPE_fbx_importer/Del_Attributes/vtxdel")
delCd.set("Cd")

#create output

output_node = mainTool.createNode("null","OUT_GEO")
output_node.setInput(0,attdel)
def_Flag = hou.node("/obj/PIPE_fbx_importer/OUT_GEO")
def_Flag.setDisplayFlag(True)

mainTool.layoutChildren()

##  <O)
##  /))
## ==#==