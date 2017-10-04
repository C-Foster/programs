import re

pat = re.compile(r"\w*ate\w*", re.I | re.M)
s = "Did you ever hear the tragedy of Darth Plagueis the Wise? It's a Sith legend. Darth Plagueis was a Dark Lord of " \
    "the Sith so powerful and so wise, that he could use the force to influence the midichlorians to create life. " \
    "He could even keep the ones he cared about from dying. " \
    "He became so powerful that the only thing he was afraid of was losing his power. " \
    "Which, eventually of course, he did. Unfortunately, he taught his apprentice everything he knew, " \
    "then his apprentice killed him in his sleep. Ironic: he could save others from death, but not himself."

matches = re.finditer(pat, s)
if matches:
    for match in matches:
        print("Found:\t{}\nAt:\t\t{}".format(match.group(), match.span()))
        print()