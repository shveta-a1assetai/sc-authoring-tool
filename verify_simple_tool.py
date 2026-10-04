import re

with open('simple_authoring_tool.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<script type="text/babel">(.*?)</script>', text, re.DOTALL)
if not m:
    print('ERROR: Babel script not found')
    exit(1)

js = m.group(1)
backtick_count = js.count('`')
brace_open = js.count('{')
brace_close = js.count('}')
paren_open = js.count('(')
paren_close = js.count(')')

print(f'Extracted JS length: {len(js)} chars')
print(f'Backticks: {backtick_count} (even: {backtick_count % 2 == 0})')
print(f'Braces: open={brace_open}, close={brace_close} (diff: {brace_open - brace_close})')
print(f'Parens: open={paren_open}, close={paren_close} (diff: {paren_open - paren_close})')
if backtick_count % 2 == 0 and brace_open == brace_close and paren_open == paren_close:
    print('>>> VALIDATION PASSED: Perfect syntax balance in simple_authoring_tool.html! <<<')
else:
    print('>>> VALIDATION FAILED! <<<')
