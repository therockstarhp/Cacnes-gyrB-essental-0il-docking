import glob, re
for f in sorted(glob.glob("*_out.pdbqt")):
    m = re.search(r"VINA RESULT:\s+(-?\d+\.\d+)", open(f).read())
    print(f, m.group(1) if m else "none")