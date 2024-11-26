import xml.etree.ElementTree as ET


def convert_ui_to_html_css(ui_file, html_file, css_file):
    tree = ET.parse(ui_file)
    root = tree.getroot()

    html_output = []
    css_output = []

    # Обрабатываем все виджеты в файле
    for widget in root.findall(".//widget"):
        widget_class = widget.get('class')
        widget_name = widget.get('name')
        html_element = None

        # Маппинг классов виджетов на HTML-теги
        if widget_class == "QLabel":
            html_element = f'<label id="{widget_name}">Label</label>'
        elif widget_class == "QPushButton":
            html_element = f'<button id="{widget_name}">Button</button>'
        elif widget_class == "QLineEdit":
            html_element = f'<input type="text" id="{widget_name}" />'
        # Добавить другие виджеты при необходимости

        if html_element:
            html_output.append(html_element)

        # Извлекаем стили из свойства 'styleSheet'
        stylesheet = widget.find(".//property[@name='styleSheet']")
        if stylesheet is not None:
            style = stylesheet.find("string").text
            if style:
                css_output.append(f"#{widget_name} {{{style}}}")

    # Записываем HTML и CSS в файлы
    with open(html_file, 'w', encoding='utf-8') as f_html:
        f_html.write("<!DOCTYPE html>\n<html>\n<body>\n")
        f_html.write("\n".join(html_output))
        f_html.write("\n</body>\n</html>")

    with open(css_file, 'w', encoding='utf-8') as f_css:
        f_css.write("\n".join(css_output))


# Пример использования
convert_ui_to_html_css('test.ui', 'output.html', 'styles.css')
