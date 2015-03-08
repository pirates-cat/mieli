def createorganization_options(command):
    command.register_option(
        '--url',
        dest='url',
        help='Agora Voting destination base URL',
        required=True)
    command.register_option(
        '--user',
        dest='user',
        help='Authentication user')
    command.register_option(
        '--token',
        dest='token',
        help='Authentication token',
        required=True)
    return command
