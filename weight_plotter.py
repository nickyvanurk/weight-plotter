#!/usr/bin/python3
import sys
import json
import matplotlib.pyplot as plt

def main():
  if len(sys.argv) > 1:
    f = open('data.json', 'r')
    d = json.load(f)
    f.close()
    f = open('data.json', 'w')
    d.insert(len(d), float(sys.argv[1]))
    json.dump(d, f)
    f.close()
  else:
    f = open('data.json', 'r')
    weight = json.load(f)
    f.close()
    if len(weight) == 0:
      return
    weeks = list(range(len(weight)))

    plt.plot(weeks, weight, marker='o')
    plt.xlabel('Weeks')
    plt.ylabel('Weight')
    plt.title('Weight Plotter')
    plt.show()

if __name__ == '__main__':
  sys.exit(main())
