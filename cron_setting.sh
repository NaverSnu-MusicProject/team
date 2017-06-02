(
  crontab -l 2>/dev/null;
  echo "SHELL=/bin/bash";
  echo "PATH=/usr/bin:/bin";
  echo "*/01 * * * * cd ~/team && python3 test.py 750"
)| crontab -
