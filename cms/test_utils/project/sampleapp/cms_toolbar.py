# -*- coding: utf-8 -*-
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK
from cms.toolbar.items import Break
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

SAMPLEAPP_BREAK = 'Sample App Break'


@toolbar_pool.register
class CategoryToolbar(CMSToolbar):
    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER)
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        if position:
            position -= 1
        else:
            position = 0
        category_menu = admin_menu.get_or_create_menu('category', _('Category'), position=position)
        category_menu.add_sideframe_item(_('Categories'), url=reverse('admin:sampleapp_category_changelist'))
        category_menu.add_modal_item(_('Add Category'), url=reverse('admin:sampleapp_category_add'))
