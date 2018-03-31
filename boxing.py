import json

with open('boxes.json', encoding="utf8") as data:
    boxes: dict = json.load(data)

NL = '\n'
WS = ' '


def boxing(text: str, style: str = 'single',
           padding: int = 1, margin: int = 1) -> str:
    chars = boxes.get(style, boxes['single'])
    lines = text.splitlines()
    max_line_len = max(map(lambda l: len(l), lines))
    margin_h, margin_v = margin * 3, margin
    padding_h, padding_v = padding * 3, padding

    vertical_margin = NL * margin_v
    horizontal_margin = WS * margin_h
    horizontal_padding = WS * padding_h

    horizontal_line = chars['horizontal'] * (max_line_len + padding_h*2)
    top_bar = horizontal_margin + chars['topLeft'] + horizontal_line + chars['topRight']
    bottom_bar = horizontal_margin + chars['bottomLeft'] + horizontal_line + chars['bottomRight']

    left = horizontal_margin + chars['vertical'] + horizontal_padding
    right = horizontal_padding + chars['vertical']

    blank_line = NL + left + WS*max_line_len + right
    vertical_padding = blank_line * padding_v

    top = vertical_margin + top_bar + vertical_padding
    middle = ''
    for line in lines:
        fill = WS * (max_line_len - len(line))
        middle += NL + left + line + fill + right
    bottom = vertical_padding + NL + bottom_bar + vertical_margin

    return top + middle + bottom
