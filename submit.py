import time
import os
import sys
import argparse
import json
import yaml
from bonnie.submission import Submission
def main():
  parser = argparse.ArgumentParser(description='Submits code to the Udacity site.')
  parser.add_argument('--provider', choices = ['gt', 'udacity'], default = 'udacity')
  parser.add_argument('--environment', choices = ['local', 'development', 'staging', 'production'], default = 'production')

  args = parser.parse_args()

  submission = Submission('cs6476', 'ps01', 
                          filenames = ["ps1.py"],
                          environment = args.environment, 
                          provider = args.provider)

  while not submission.poll():
    time.sleep(3.0)

  if submission.feedback():
    feedback = submission.result()
    print feedback['console_summary']
  elif submission.error_report():
    error_report = submission.error_report()
    print json.dumps(error_report, indent=4)
  else:
    print "Unknown error."

if __name__ == '__main__':
  main()
