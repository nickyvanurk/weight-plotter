#!/usr/bin/python3
import sys
import json
import matplotlib.pyplot as plt
import parser
import argparse
import collections
import numpy

def get_command_line_args():
  defaults = {'weight': '', 'goal': '', 'weeks': ''}
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', dest='weight', help='your current weight')
  parser.add_argument('-g', dest='goal', help='your ideal weight')
  parser.add_argument('-w', dest='weeks', help='weeks until goal')
  command_line_args = {k:v for k, v in vars(parser.parse_args()).items() if v}
  return collections.ChainMap(command_line_args, defaults)

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
  args = get_command_line_args()
  current_weight = args['weight'].strip()
  ideal_weight = args['goal'].strip()
  weeks_until_goal = args['weeks'].strip()

  if current_weight:
    add_weight(float(current_weight), 'data.json')
  else:
    weight = get_data('data.json')
    if weight:
      weeks = list(range(len(weight)))
      if ideal_weight and weeks_until_goal:
        step_size = (float(ideal_weight) - weight[0]) / int(weeks_until_goal)
        data = list(numpy.arange(weight[0], float(ideal_weight) + step_size, step_size))
        plt.plot(list(range(int(weeks_until_goal)+1)), data, marker='o',
                                                             linestyle='--',
                                                             label='Goal')
      plt.plot(weeks, weight, marker='o', label='Weight')
      plt.xlabel('Weeks')
      plt.ylabel('Weight')
      plt.title('Weight Plotter')
      plt.legend(loc=2)
      plt.show()

if __name__ == '__main__':
  sys.exit(main())
