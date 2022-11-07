if __name__ == "__main__":
    try:
        with open('/Users/benoitboidin/Desktop/cremi_server_names.txt') as input_file:
            lines = input_file.readlines()
            with open('cremi_config.txt', 'w+') as output_file:
                for name in lines:
                    name = name.replace('\n', '')
                    print('Adding {} to config file.'.format(name))
                    output_file.write('Host' + name + '\n  HostName'+ name + '.emi.u-bordeaux.fr\n  User bboidin\n  ProxyJump cremi\n  ForwardX11 yes\n\n')

    except TypeError:
        print("Error")