##############################
# import
##############################
import wx

import GUI_Draw
import sys
import ctypes
try:
	ctypes.windll.shcore.SetProcessDpiAwareness(True)
except Exception:
	pass

from gsnodegraph import EVT_GSNODEGRAPH_ADDNODEBTN
from nodes import OutputNode, MixNode, ImageNode, BlurNode, BlendNode, ValueNode
from nodegraph import NodeGraph

# Install a custom displayhook to keep Python from setting the global
# _ (underscore) to the value of the last evaluated expression.
# If we don't do this, our mapping of _ to gettext can get overwritten.
# This is useful/needed in interactive debugging with PyShell.
def _displayHook(obj):
	""" Custom display hook to prevent Python stealing '_'. """

	if obj is not None:
		print(repr(obj))

# Add translation macro to builtin similar to what gettext does.
import builtins
builtins.__dict__['_'] = wx.GetTranslation


class MainApp(wx.App):

	def OnInit(self):

		# Work around for Python stealing "_".
		sys.displayhook = _displayHook

		return True

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Draw.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Draw.Main.__init__(self, parent)
		node_registry = {
			"image_nodeid": ImageNode,
			"mix_nodeid": MixNode,
			"blur_nodeid": BlurNode,
			"blend_nodeid": BlendNode,
			"value_nodeid": ValueNode,
			"output_nodeid": OutputNode
		}
		# Setup the config with datatypes and node categories
		config = {
			"image_datatype": "IMAGE",
			"node_datatypes": {
				"IMAGE": "#C6C62D",  # Yellow
				"INTEGER": "#A0A0A0",  # Grey
				"FLOAT": "#A0A0A0",  # Grey
				"VALUE": "#A0A0A0",  # Depreciated!
			},
			"node_categories": {
				"INPUT": "#E64555",  # Burgendy
				"DRAW": "#AF4467",  # Pink
				"MASK": "#084D4D",  # Blue-green
				"CONVERT": "#564B7C",  # Purple
				"FILTER": "#558333",  # Green
				"BLEND": "#498DB8",  # Light blue
				"COLOR": "#C2AF3A",  # Yellow
				"TRANSFORM": "#6B8B8B", # Blue-grey
				"OUTPUT": "#B33641"  # Red
			}
		}

		# Init the nodegraph
		print(self)
		ng = NodeGraph(parent=self, registry=node_registry, config=config,size=(500,500))

		# Add nodes to the node graph
		node1 = ng.AddNode("image_nodeid", pos=wx.Point(100, 10))
		node2 = ng.AddNode("image_nodeid", pos=wx.Point(450, 400))
		node3 = ng.AddNode("mix_nodeid", pos=wx.Point(400, 100))
		node4 = ng.AddNode("blur_nodeid", pos=wx.Point(700, 100))
		node5 = ng.AddNode("blend_nodeid", pos=wx.Point(720, 300))
		node6 = ng.AddNode("value_nodeid", pos=wx.Point(620, 430))
		node7 = ng.AddNode("output_nodeid", pos=wx.Point(1000, 290))

	def Close(self, event):
		try:
			if app.GetAppName() != '_core.cp38-win_amd64':
				self.Destroy()
		except:
			self.Hide()

##############################
# 主函数
##############################


def main():
	global app
	app = MainApp(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()


if __name__ == "__main__":
	main()
