#!/usr/bin/python3
import sys
import json
import matplotlib.pyplot as plt

def has_argument():
  return len(sys.argv) > 1

def get_data(file):
  with open(file, 'r') as f:
    try:
      return json.load(f)
    except:
      return []

def write_data(data, file):
  with open(file, 'w') as f:
    json.dump(data, f)

def add_weight(weight, file):
  d = get_data(file)
  d.insert(len(d), weight)
  write_data(d, file)

def main():
  if has_argument():
    add_weight(float(sys.argv[1]), 'data.json')
  else:
    weight = get_data('data.json')
    if weight:
      weeks = list(range(len(weight)))
      plt.plot(weeks, weight, marker='o')
      plt.xlabel('Weeks')
      plt.ylabel('Weight')
      plt.title('Weight Plotter')
      plt.show()

if __name__ == '__main__':
  sys.exit(main())
