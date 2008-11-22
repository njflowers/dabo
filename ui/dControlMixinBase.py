# -*- coding: utf-8 -*-
""" dControlMixin.py: Provide behavior common to all dControls """

import dabo
import dabo.ui
from dabo.dLocalize import _
import dabo.dEvents as dEvents

class dControlMixinBase(dabo.ui.dPemMixin):
	""" Provide common functionality for all controls.
	"""
	def _initEvents(self):
		super(dControlMixinBase, self)._initEvents()
		
		self.bindEvent(dEvents.GotFocus, self.__onGotFocus)

	def __onGotFocus(self, evt):
		if self.Form:
			sfac = self.Form.ActiveControl  ## cache current ac
			self.Form._activeControl = self ## set new ac
			if sfac is not None and sfac is not self:
				# make sure prior control's value has been flushed
				self.Form.activeControlValid()
		if self.Parent:
			self.Parent._activeControl = self

