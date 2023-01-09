""" Command line interface for Eva High Level API """

from __future__ import print_function
import argparse
import json
import eva

COMMAND_HOMES = 'homes'
COMMAND_HOME = 'home'


def print_result(overview, *names):
    """ Print the result of a eva request """
    if names:
        for name in names:
            toprint = overview
            for part in name.split('/'):
                toprint = toprint[part]
            print(json.dumps(toprint, indent=4, separators=(',', ': ')))
    else:
        print(json.dumps(overview, indent=4, separators=(',', ': ')))


# pylint: disable=too-many-locals,too-many-statements
def main():
    """ Start eva command line """
    parser = argparse.ArgumentParser(
        description='Read or change status of eva devices')
    parser.add_argument(
        'username',
        help='Eva app username')
    parser.add_argument(
        'password',
        help='Eva app password')
    parser.add_argument(
        'environment',
        help='Eva environment',
        default='https://home-hla.evasmart.no')
    parser.add_argument(
        '-i', '--home-id',
        help='Eva home id')
    parser.add_argument(
        '-c', '--cookie',
        help='File to store cookie in',
        default='~/.eva-cookie')

    commandsparser = parser.add_subparsers(
        help='commands',
        dest='command')

    # homes command
    commandsparser.add_parser(
        COMMAND_HOMES,
        help='Get homes')

    # devices command
    commandsparser.add_parser(
        COMMAND_HOME,
        help='Get home')

    args = parser.parse_args()
    session = eva.Session(args.username, args.password, args.environment, args.home_id, args.cookie)
    try:
        if args.command == COMMAND_HOMES:
            session.homes = session._get_homes()
            print_result("Available homes:")
            for home in session.homes:
                print_result(home["name"] + " (id: " + home["id"] + ")")
        if args.command == COMMAND_HOME:
            session.home = session._get_home(args.home_id)
            print_result("Devices in home " + session.home["name"] + ":")
            for room in session.home["rooms"]:
                for device in room["devices"]:
                    print_result(device["name"])

    except eva.session.ResponseError as ex:
        print(ex.text)


# pylint: disable=C0103
if __name__ == "__main__":
    main()
