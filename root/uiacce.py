# Search def OnOverInItem(self, selectedSlotPos): in class CombineWindow
# after:

		if self.tooltipItem:
			if selectedSlotPos == acce.WINDOW_MAX_MATERIALS:
				(isHere, iCell) = acce.GetAttachedItem(0)
				if isHere:

#add:

					self.tooltipItem.ClearToolTip()
					self.tooltipItem.SetInventoryItem(iCell)

# Search def OnOverInItem(self, selectedSlotPos): in class AbsorbWindow
# after :

		if self.tooltipItem:
			if selectedSlotPos == acce.WINDOW_MAX_MATERIALS:
				(isHere1, iCell1) = acce.GetAttachedItem(0)
				(isHere2, iCell2) = acce.GetAttachedItem(1)
				if isHere1 and isHere2:

# add:

					self.tooltipItem.ClearToolTip()
					self.tooltipItem.SetInventoryItem(iCell1)