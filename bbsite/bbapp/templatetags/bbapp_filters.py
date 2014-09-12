from django import template
import sys

register = template.Library()

@register.filter(name='get_pag_list')
def get_pag_list(value, arg):
	''' value=number_of_pages, arg=current_page, plist=list of five pages around of current_page '''
	if arg <= 2:
		plist = value[0 : 5]
	else:
		plist = value[arg - 3 : arg + 2]

	if arg >= len(value) - 2:
		plist = value[len(value) - 5 : len(value)]
		
	return plist