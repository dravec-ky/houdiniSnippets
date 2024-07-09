import hou
import objecttoolutils

createdNode = kwargs["node"]

#https://forums.odforce.net/topic/28579-python-node-placement/

# python code inside an OnCreated script

# get current network pane
net_editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)

# get cursor position
position = net_editor.cursorPosition()

# create your node
renderNode = hou.node(".").createNode("null", "OUT_Render", 0, 0)
displayNode = hou.node(".").createNode("null", "OUT_Display", 0, 0)

#Set node position
x_offset = -0.5
offset_left = hou.Vector2(-2 + x_offset,-1)
offset_right = hou.Vector2(2 + x_offset,-1)

renderNode.setPosition(position + offset_left)
displayNode.setPosition(position + offset_right)

#Connect Nodes
renderNode.setInput(0, createdNode,0)
displayNode.setInput(0, createdNode,1)

renderNode.setRenderFlag(True)
displayNode.setDisplayFlag(True)
