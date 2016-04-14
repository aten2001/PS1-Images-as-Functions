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
  parser.add_argument('--environment', choices = ['local', 'development', 'staging', 'production'], default = 'development')

  args = parser.parse_args()

  app_data_dir = os.path.abspath(".bonnie")

  submission = Submission('cs6476', 'ps01', 
                          filenames = ["ps1.py"], 
                          exclude = False, 
                          environment = args.environment, 
                          provider = args.provider,
                          app_data_dir = app_data_dir)

  while not submission.poll():
    time.sleep(3.0)

  if submission.result():
    result = submission.result()
    print json.dumps(result, indent=4)
  elif submission.error_report():
    error_report = submission.error_report()
    print json.dumps(error_report, indent=4)
  else:
    print "Unknown error."

if __name__ == '__main__':
  main()
