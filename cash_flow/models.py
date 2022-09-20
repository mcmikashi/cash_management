from django.db import models
from django.utils.translation import gettext as _



class Category(models.Model):
    label = models.CharField(_("label"), max_length=255)
    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.label




class Transaction(models.Model):

    label = models.CharField(_("lable"), max_length=255)
    date = models.DateField(_("date"))
    amount = models.DecimalField(_("amount"), max_digits=14, decimal_places=2)
    tax = models.DecimalField(_("tax"), max_digits=5, decimal_places=2)
    category = models.ForeignKey(
        "cash_flow.Category", verbose_name=_("category"), 
        related_name="transaction", on_delete=models.SET_NULL, 
        null=True, blank=True)

    @property
    def including_tax(self) -> float:
        "Returns the including tax of the transaction."
        return round(self.amount + (self.amount * (self.tax / 100)), 2)

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")

    def __str__(self):
        return f"{self.label} - {self.including_tax} - {self.date}"
