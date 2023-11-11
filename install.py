import subprocess
libraries_to_install = ['pygetwindow', 'time', 'socket', 'threading', 'json']
for library in libraries_to_install:
    try:
        subprocess.run(['pip', 'install', library], check=True)
        print(f'{library} has been successfully installed.')
    except subprocess.CalledProcessError:
        print(f'Failed to install {library}.')