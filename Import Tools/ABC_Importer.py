##abcimporter
import hou

#Root node
setRoot = hou.node("/obj")

#create tool node
mainTool = setRoot.createNode("geo", "PIPE_abc_importer")
mainTool.setColor(hou.Color((0.18,0.31,0.62)))
mainTool.setUserData("nodeshape", "circle")


#create importer

importer = mainTool.createNode("alembic","Input")
importer.moveToGoodPosition()

#create transform

transform = mainTool.createNode("xform", "scale")
transform.setInput(0,importer)
scale = hou.parm("/obj/PIPE_abc_importer/scale/scale")
scale.set(0.01)

#create unpack

unpack = mainTool.createNode("unpack","unpack_geo")
unpack.setInput(0,transform)
trans_att = hou.parm("/obj/PIPE_abc_importer/unpack_geo/transfer_attributes")
trans_grp = hou.parm("/obj/PIPE_abc_importer/unpack_geo/transfer_groups")
trans_att.set("*")
trans_grp.set("*")

#create convert

convert_node = mainTool.createNode("convert", "convert_geo")
convert_node.setInput(0,unpack)

#create output

output_node = mainTool.createNode("null","OUT_GEO")
output_node.setInput(0,convert_node)
def_Flag = hou.node("/obj/PIPE_abc_importer/OUT_GEO")
def_Flag.setDisplayFlag(True)

mainTool.layoutChildren()


##  <O)
##  /))
## ==#==
