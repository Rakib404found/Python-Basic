letter = '''Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Rakibul").replace("<|Date|>", "15 May, 2025"))

print(letter.replace("<|Name|>", "Rakibul").replace("<|Date|>", "15 May 2025"))