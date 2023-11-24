from nicegui import ui

from ..model import UiElementDocumentation


class MarkdownDocumentation(UiElementDocumentation, element=ui.markdown):

    def main_demo(self) -> None:
        ui.markdown('''This is **Markdown**.''')

    def more(self) -> None:
        @self.add_markdown_demo('Markdown with indentation', '''
            Common indentation is automatically stripped from the beginning of each line.
            So you can indent markdown elements, and they will still be rendered correctly.
        ''')
        def markdown_with_indentation():
            ui.markdown('''
                ### Example

                This line is not indented.

                    This block is indented.
                    Thus it is rendered as source code.
                
                This is normal text again.
            ''')

        @self.add_markdown_demo('Markdown with code blocks', '''
            You can use code blocks to show code examples.
            If you specify the language after the opening triple backticks, the code will be syntax highlighted.
            See [the Pygments website](https://pygments.org/languages/) for a list of supported languages.
        ''')
        def markdown_with_code_blocks():
            ui.markdown('''
                ```python
                from nicegui import ui

                ui.label('Hello World!')

                ui.run(dark=True)
                ```
            ''')

        @self.add_markdown_demo('Markdown tables', '''
            By activating the "tables" extra, you can use Markdown tables.
            See the [markdown2 documentation](https://github.com/trentm/python-markdown2/wiki/Extras#implemented-extras) for a list of available extras.
        ''')
        def markdown_tables():
            ui.markdown('''
                | First name | Last name |
                | ---------- | --------- |
                | Max        | Planck    |
                | Marie      | Curie     |
            ''', extras=['tables'])
