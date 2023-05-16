import sys

lain = r"""
          _..--¯¯¯¯--.._
      ,-''              `-.
    ,'                     `.
   ,                         \
  /                           \
 /          ′.                 \
'          /  ││                ;
;       n /│  │/         │      │
│      / v    /\/`-'v√\'.│\     ,
:    /v`,———         ————.^.    ;
'   │  /′@@`,        ,@@ `\│    ;
│  n│  '.@@/         \@@  /│\  │;
` │ `    ¯¯¯          ¯¯¯  │ \/││
 \ \ \                     │ /\/
 '; `-\          `′       /│/ │′
  `    \       —          /│  │
   `    `.              .' │  │
    v,_   `;._     _.-;    │  /
       `'`\│-_`'-''__/^'^' │ │        
              ¯¯¯¯¯        │/
"""

bubble_stem = r"""
|
 \
  \_______
"""

if len(sys.argv) > 1:
    text = sys.argv[1]
else:
    print("You must provide at least one argument!")
    sys.exit(0)

broken_text = ""
line_length = 0
for word in text.split(" "):
    line_length += len(word) + 1
    if line_length > 40:
        broken_text += "\n"
        line_length = 0
    broken_text += word + " "

lines = broken_text.split("\n")
if len(lines) == 1:
    formatted_text = "< " + broken_text + " >"
else:
    formatted_text = ""
    for l in range(len(lines)):
        if l == 0:
            edges = ("/", "\\")
        elif l == len(lines) - 1:
            edges = ("\\", "/")
        else:
            edges = ("|", "|")

        formatted_text += edges[0] + " " + lines[l] + " " + edges[1] + "\n"

formatted_text = .....