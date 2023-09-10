from docutils import nodes
import jinja2
from docutils.parsers.rst.directives import unchanged
from docutils.parsers.rst import Directive
from sphinx.application import Sphinx
from docutils.parsers.rst import roles
from docutils.parsers.rst.states import Inliner
from typing import List, Dict
import re

BUTTON_TEMPLATE = jinja2.Template("""
{% if link  %} 
    <a href="{{ link }}">    
        <button class="{{ class }}" {{ style |default('') }}>{{ text }}</button>
    </a>
{% else %}
    <button class="{{ class }}" {{ style |default('') }}>{{ text }}</button>
{% endif %}
""")


# placeholder node for document graph
class ButtonNode(nodes.Element):
    ...


class ButtonDirective(Directive):
    has_content = True
    required_arguments = 0

    option_spec = {
        'link': unchanged,
        'class': unchanged,
        'style': unchanged,
    }

    # this will execute when your directive is encountered
    # it will insert a ButtonNode into the document that will
    # get visisted during the build phase
    def run(self):
        env = self.state.document.settings.env
        app: Sphinx = env.app
        app.add_css_file('button.css')  # or you can set it on the conf.py

        node = ButtonNode()
        node['text'] = ''.join(self.content.data)
        node['class'] = self.options['class'].strip()
        node['link'] = self.options.get('link')
        if self.options.get('style'):
            style = 'style=' + self.options['style'] 
            node['style'] = style
        return [node]


# build phase visitor emits HTML to append to output
def html_visit_button_node(self, node: ButtonNode):
    # html = BUTTON_TEMPLATE.render(text=node['text'], link=node['link'])
    html = BUTTON_TEMPLATE.render({k: v for k, v in node.attributes.items()})
    self.body.append(''.join([_.strip() for _ in html.split('\n') if _.strip()]))
    raise nodes.SkipNode


def button_role(role, rawtext, text, line_no, in_liner: Inliner, options: Dict = None, content: List = None):
    # 'link="https://www.google.com/" style="background-color:green; font-size: 30px;"'
    regex = re.compile(f"(?:.*"
                       fr"(?P<link>link=\S*)|"
                       fr"(?P<style>style=\S*)"
                       f")",
                       )

    text, cls, *options = text.split('|')
    node = ButtonNode()  # nodes.paragraph
    node['class'] = cls.strip()
    node['text'] = text.rstrip()

    if options:
        options: str = options[0].strip()
        for attr in options.split(' '):
            m = regex.match(attr)
            if m:
                dict_option = m.groupdict()
                if dict_option.get('link'):
                    dict_option['link'] = dict_option['link'][5:]  # remove link=
                for key, value in dict_option.items():
                    if value:
                        node[key] = value.strip()
    return [node], []


def setup(app: Sphinx):

    """
    .. button::
        option1:
        option2:
    """
    app.add_node(ButtonNode,
                 # ↓ kwargs
                 html=(html_visit_button_node, lambda: None)
                 # other_2: Tuple[Callable, Callable],
                 # other_3: Tuple[visit_xxx, depart_xxx],
                 )
    app.add_directive('button', ButtonDirective)

    """
    :btn:``
    """
    roles.register_canonical_role('btn', button_role)