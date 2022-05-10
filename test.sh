#!/bin/bash

for py_file in $(find ./hometask -name *.py); do
  if [[ "$py_file" == *"__"* ]]; then
    continue
  fi
  echo "Run $py_file"
  python $py_file
done

echo 'All Done!'