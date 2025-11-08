import os, subprocess, sys
BAD = os.getenv("BAD_HASH", "c1a4be04b972b6c17db242fc37752ad517c29402")
GOOD = os.getenv("GOOD_HASH","e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")

def sh(cmd):
    return subprocess.run(cmd, shell=True, check=False).returncode

if sh("pip install -r requirements.txt") != 0:
    sys.exit(125)

rc = sh(f"git bisect start {BAD} {GOOD}") or \
     sh("git bisect run bash -lc 'python manage.py test'")

sys.exit(0 if rc == 0 else 1)
