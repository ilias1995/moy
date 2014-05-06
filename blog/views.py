from django.shortcuts import render

def display_meta(request):
	values = request.МЕТА.items()
	values.sort()
	html = []
	for k, v in values:
	html.append('<trxtd>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % *'\n'.join(html))
