import re

# Markdown格式的文本
markdown_text = """
| Name | Age | Gender |
|------|-----|--------|
| John | 25  | Male   |
| Jane | 30  | Female |
"""

# 正则表达式匹配Markdown表格
table_regex = re.compile(r'\|(.+)\|')
table_matches = table_regex.findall(markdown_text)

# 提取表格数据
table_data = []
for row in table_matches:
    table_data.append([cell.strip() for cell in row.split('|') if cell.strip()])

# 输出行数和列数
num_rows = len(table_data)
num_cols = len(table_data[0])
print(f"Table has {num_rows} rows and {num_cols} columns.")