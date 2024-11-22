# Title: gltf-validator
# Version: 1.0.0
# Publisher: NFDI4Culture
# Publication date: December 20, 2023
# License: CC BY 4.0

from __future__ import print_function
import json
import subprocess
import sys


class GLTFValidatorException(Exception):
    pass

def parse_gltf_validator_data(target):
    validator_path = '/usr/share/gltf_validator'
    args = [validator_path, '-amo', target]
    try:
        output = subprocess.check_output(args).decode("utf8")
    except subprocess.CalledProcessError:
        raise GLTFValidatorException("gltf_validator failed when running: " + ' '.join(args))
    return json.loads(output.encode("utf8"))

def get_issues(doc):
    if not "issues" in doc:
       raise GLTFValidatorException("Unable to find issues!")
    return doc["issues"]

def get_outcome(issues, format=None):
    if issues["numErrors"] == 0: # and issues["numWarnings"] == 0:
        return "pass"
    else:
        return "fail"

def get_format(doc):
    format = doc["mimeType"]
    version = doc["info"]["version"]
    return (format, version)

def format_event_outcome_detail_note(format, version, result):
    note = 'format="{}";'.format(format)
    if version is not None:
        note = note + ' version="{}";'.format(version)
    note = note + ' result="{}"'.format(result)

    return note

def main(target):
    try:
        doc = parse_gltf_validator_data(target)
        issues = get_issues(doc)
        format, version = get_format(doc)
        outcome = get_outcome(issues, format)
        note = format_event_outcome_detail_note(format, version, issues)

        out = {
            "eventOutcomeInformation": outcome,
            "eventOutcomeDetailNote": note
        }
        print(json.dumps(out))

        return 0
    except GLTFValidatorException as e:
        return e

if __name__ == '__main__':
    target = sys.argv[1]
    sys.exit(main(target))
