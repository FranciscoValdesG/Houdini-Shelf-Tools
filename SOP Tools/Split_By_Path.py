##select node
selNodes = hou.selectedNodes()


#check Selection
if len(selNodes)==1:
    selState = True
if len(selNodes)==0:
    selState = False
if len(selNodes)>1:
    selState = False
    

if selState == False:
    hou.ui.displayMessage("Select geometry source node")
else:
    #get geometry
    objNode = selNodes[0]
    objNode = objNode.geometry()
    pathAtt = objNode.findPrimAttrib("path").strings()
    #Split Object for every path group 
    sourceNode = selNodes[0].parent()
    mergeNode = sourceNode.createNode("merge", "Merge")
    for path in pathAtt:
        pathSplit = path.split("/")[0]
        blastNode = sourceNode.createNode("blast", f"blast{pathSplit}")
        blastNode.parm("negate").set(1)
        blastNode.parm("group").set(f"@path={pathSplit}/*")
        blastNode.setInput(0,selNodes[0])
        outBlastNode = sourceNode.createNode("null", f"OUT_{pathSplit}")
        outBlastNode.setInput(0,blastNode)
        mergeNode.setNextInput(outBlastNode,0)
    outNode = sourceNode.createNode("null", "OUT_Preview")
    outNode.setInput(0,mergeNode)
    outNode.setRenderFlag(True)
    outNode.setDisplayFlag(True)
    selNodes[0].moveToGoodPosition()
    selNodes[0].parent().layoutChildren()
    hou.ui.displayMessage("Have a Nice Day!!")