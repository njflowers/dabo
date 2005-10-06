import wx, dabo, dabo.ui

if __name__ == "__main__":
	dabo.ui.loadUI("wx")

import dDataControlMixin as dcm
import dabo.dEvents as dEvents
from dabo.dLocalize import _

	
class dCheckBox(wx.CheckBox, dcm.dDataControlMixin):
	""" Allows visual editing of boolean values.
	"""
	def __init__(self, parent, properties=None, *args, **kwargs):
		self._baseClass = dCheckBox
		preClass = wx.PreCheckBox
		dcm.dDataControlMixin.__init__(self, preClass, parent, properties, *args, **kwargs)

	
	def _initEvents(self):
		super(dCheckBox, self)._initEvents()
		self.Bind(wx.EVT_CHECKBOX, self._onWxHit)
	
			
	def _onWxHit(self, evt):
		self.flushValue()
		dCheckBox.doDefault(evt)

		
	# property get/set functions
	def _getAlignment(self):
		if self._hasWindowStyleFlag(wx.ALIGN_RIGHT):
			return "Right"
		else:
			return "Left"

	def _setAlignment(self, value):
		self._delWindowStyleFlag(wx.ALIGN_RIGHT)
		if str(value) == "Right":
			self._addWindowStyleFlag(wx.ALIGN_RIGHT)
		elif str(value) == "Left":
			pass
		else:
			raise ValueError, "The only possible values are 'Left' and 'Right'."

		
	# property definitions follow:
	Alignment = property(_getAlignment, _setAlignment, None,
		"""Specifies the alignment of the text.
			
		Left  : Checkbox to left of text (default)
		Right : Checkbox to right of text
		""")


class _dCheckBox_test(dCheckBox):
			def initProperties(self):
				self.Caption = "Do you wish to pass?"
				self.Width = 222			

if __name__ == "__main__":
	import test
	test.Test().runTest(_dCheckBox_test)
