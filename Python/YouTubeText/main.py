# The motive for this code was to clean the transcripts of YouTube videos, simply by removing the time tags.

# open the text file
i_name = "tm.txt"
o_name = "tm_ready.txt"

picked_lines = []
with open(i_name, "r", errors="ignore") as fi:
    i = 1
    for line in fi:
        if i % 2 == 0:
            picked_lines.append(line.strip())
        i += 1

with open(o_name, "w") as fo:
    fo.write(" ".join(picked_lines))
