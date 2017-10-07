import re

abc = re.compile(r"[0-9]?x\^2\s?[+-]\s?[0-9]x\s?[+-]\s?[0-9]")  # ax^2 + bx + c
ab = re.compile(r"[0-9]?x\^2\s?[+-]\s?[0-9]x")  # ax^2 + bx
ac = re.compile(r"[0-9]?x\^2\s?-\s?[0-9]")  # ax^2 - c

equation = "x^2 - 12"

m_abc = re.match(abc, equation)
m_ab = re.match(ab, equation)
m_ac = re.match(ac, equation)

if m_abc:
    print(m_abc.group())
    print("It is of the form 'ax^2 + bx + c'")
elif m_ab:
    print(m_ab.group())
    print("It is of the form 'ax^2 + bx'")
elif m_ac:
    print(m_ac.group())
    print("It is of the form 'ax^2 - c'")
else:
    print("Equation invalid.")