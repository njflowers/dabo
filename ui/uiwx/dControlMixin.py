from dabo.ui.dControlMixinBase import dControlMixinBase
import dabo.dEvents as dEvents

class dControlMixin(dControlMixinBase):
	
	def _onWxHit(self, event):
		self.raiseEvent(dEvents.Hit, event)
		event.Skip()
		
