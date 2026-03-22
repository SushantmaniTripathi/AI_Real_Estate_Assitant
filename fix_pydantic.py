"""Fix Pydantic v2 compatibility in hybrid_retriever.py"""

import re

# Read the file
with open(r'd:\Agents_Biz\Trading_git\ai-real-estate-assistant\vector_store\hybrid_retriever.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the old Config class with model_config
old_pattern = r'(\s+)class Config:\s+arbitrary_types_allowed = True'
new_config = r'\1model_config = {"arbitrary_types_allowed": True}'

content = re.sub(old_pattern, new_config, content)

# Write back
with open(r'd:\Agents_Biz\Trading_git\ai-real-estate-assistant\vector_store\hybrid_retriever.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Pydantic v2 compatibility")
