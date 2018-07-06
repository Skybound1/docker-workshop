import webbrowser
import glob
from jinja2 import Environment


TEMPLATE = open('template/slideshow.html.j2').read()


sections = []
for index, sfile in enumerate(sorted(glob.glob('sections/*.md'))):
    section = open(sfile).read()

    if index > 0 and not section.startswith('---'):
        section = '---\n' + section

    sections.append(section)


with open('slideshow.html', 'w+') as sfh:
    print(Environment().from_string(TEMPLATE).render(sections=sections), file=sfh)


webbrowser.open('slideshow.html')
