def createuser_options(command):
    command.register_option(
        '--location',
        dest='location',
        help='Geoname ID for user location',
        required=False)
    return command
