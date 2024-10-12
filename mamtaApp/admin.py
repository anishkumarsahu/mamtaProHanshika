from django.contrib import admin

# Register your models here.
from .models import *

class StaffTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'datetime', ]
admin.site.register(StaffType, StaffTypeAdmin)


class AdminAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'password', 'lastUpdatedOn', ]


admin.site.register(Admin, AdminAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phoneNumber', 'isActive', 'lastUpdatedOn']


admin.site.register(StaffUser, StaffAdmin)


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phoneNumber', 'closingBalance', 'datetime']


admin.site.register(Buyer, BuyerAdmin)

class CreditAdmin(admin.ModelAdmin):
    list_display = ['buyerID','amount','remark','datetime']

admin.site.register(MoneyToCollect,CreditAdmin)

class DebitAdmin(admin.ModelAdmin):
    list_display = ['buyerID','collectedBy','amount','remark','datetime']

admin.site.register(MoneyCollection,DebitAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','phoneNumber','address','datetime']

admin.site.register(Company,CompanyAdmin)


class CashMoneyCollectionAdmin(admin.ModelAdmin):
    list_display = ['buyerID','collectedBy','amount','remark','datetime']

admin.site.register(CashMoneyCollection,CashMoneyCollectionAdmin)



class SupplyCollectionAdmin(admin.ModelAdmin):
    list_display = ['amount','collectedBy','buyerID','remark','Location','datetime']

admin.site.register(SupplierCollection,SupplyCollectionAdmin)


class SupplierInvoiceCollectionAdmin(admin.ModelAdmin):
    list_display = ['amount','collectedBy','buyerID','remark','Location','datetime']

admin.site.register(SupplierInvoiceCollection,SupplierInvoiceCollectionAdmin)


class LoginAndLogoutAdmin(admin.ModelAdmin):
    list_display = ['userID','statusType','isDeleted','datetime']

admin.site.register(LoginAndLogoutStatus,LoginAndLogoutAdmin)


class StaffAdvanceToBuyerAdmin(admin.ModelAdmin):
    list_display = ['buyerID','amount','isDeleted','datetime']

admin.site.register(StaffAdvanceToBuyer,StaffAdvanceToBuyerAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ['instanceID', 'apiKey', 'balance', 'used', 'datetime', 'lastUpdatedOn', 'isDeleted']


admin.site.register(WhatsappMessage, MessageAdmin)


class MessageStatusAdmin(admin.ModelAdmin):
    list_display = ['messageTo', 'phone', 'status', 'message', 'datetime', 'lastUpdatedOn', 'isDeleted']


admin.site.register(WhatsappMessageStatus, MessageStatusAdmin)