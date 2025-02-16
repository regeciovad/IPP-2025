import sys

print('42: fatal error', file=sys.stderr)
sys.exit(42) # echo $? will show 42
