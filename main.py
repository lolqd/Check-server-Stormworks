import os, json, subprocess, pygetwindow as gw, time, socket, threading

datatowrite = {
    "Stormworks":{
        "Servers": {
            "1_Server": "dir",
            "2_Server": "dir",
            "3_Server": "dir",
            "4_Server": "dir",
            "1_Server_title": "title",
            "2_Server_title": "title",
            "3_Server_title": "title",
            "4_Server_title": "title",
        },
    }, 
    "Settings": {
        "server_1_enable": "False",
        "server_2_enable": "False",
        "server_3_enable": "False",
        "server_4_enable": "False",
        "Port": "601",
        "time_to_check_servers": 30, # seconds to check server
        }
}

timer_running_1 = False
timer_running_2 = False
timer_running_3 = False
timer_running_4 = False

folder_name = "data"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

filename = os.path.join(folder_name, "config.json")
if not os.path.isfile(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(datatowrite, f, indent=4)
        
with open(filename, 'r', encoding='utf-8') as f:
    config = json.load(f)
    global server_1_dir, server_2_dir, server_3_dir, server_4_dir, server_1_title, server_2_title, server_3_title, server_4_title, server_1_enabled, server_2_enabled
    global server_3_enable, server_4_enable, Port, time_to_check_servers

    server_1_dir = config["Stormworks"]["Servers"]["1_Server"]
    server_2_dir = config["Stormworks"]["Servers"]["2_Server"]
    server_3_dir = config["Stormworks"]["Servers"]["3_Server"]
    server_4_dir = config["Stormworks"]["Servers"]["4_Server"]
    server_1_title = config["Stormworks"]["Servers"]["1_Server_title"]
    server_2_title = config["Stormworks"]["Servers"]["2_Server_title"]
    server_3_title = config["Stormworks"]["Servers"]["3_Server_title"]
    server_4_title = config["Stormworks"]["Servers"]["4_Server_title"]
    server_1_enable = config["Settings"]["server_1_enable"]
    server_2_enable = config["Settings"]["server_2_enable"]
    server_3_enable = config["Settings"]["server_3_enable"]
    server_4_enable = config["Settings"]["server_4_enable"]
    Port = int(config["Settings"]["Port"])
    time_to_check_servers = int(config["Settings"]["time_to_check_servers"])   
    
def server_1_restart():
    print("restarting 1 server...")
    window = gw.getWindowsWithTitle(server_1_title)
    if window:
        window[0].close()
    os.chdir(os.path.dirname(server_1_dir))
    subprocess.Popen(['start', 'cmd', '/c',server_1_dir], shell=True)
    
def server_2_restart():
    print("restarting 2 server...")
    window = gw.getWindowsWithTitle(server_2_title)
    if window:
        window[0].close()
    os.chdir(os.path.dirname(server_2_dir))
    subprocess.Popen(['start', 'cmd', '/c',server_2_dir], shell=True)
    
def server_3_restart():
     print("restarting 3 server...")
     window = gw.getWindowsWithTitle(server_3_title)
     if window:
         window[0].close()
     os.chdir(os.path.dirname(server_3_dir))
     subprocess.Popen(['start', 'cmd', '/c',server_3_dir], shell=True)

def server_4_restart():
     print("restarting 4 server...")
     window = gw.getWindowsWithTitle(server_4_title)
     if window:
         window[0].close()
     os.chdir(os.path.dirname(server_4_dir))
     subprocess.Popen(['start', 'cmd', '/c',server_4_dir], shell=True)

def timer_thread_1():
    global last_reset_time_1
    if timer_running_1:
        print("timer thread 1 started")
        while True:
                current_time = time.time()
                if current_time - last_reset_time_1 >= time_to_check_servers:
                    print("server 1 offline go to restart...")
                    last_reset_time_1 = current_time
                    server_1_restart()
                time.sleep(1)

def timer_thread_2():
    global last_reset_time_2
    if timer_running_2:
        print("timer thread 2 started")
        while True:           
            current_time = time.time()
            if current_time - last_reset_time_2 >= time_to_check_servers:
                print("server 2 offline go to restart...")
                last_reset_time_2 = current_time
                server_2_restart()
            time.sleep(1)

def timer_thread_3():
    global last_reset_time_3
    if timer_running_3:
        print("timer thread 3 started")
        while True:
            current_time = time.time()
            if current_time - last_reset_time_3 >= time_to_check_servers:
                print("server 3 offline go to restart...")
                last_reset_time_3 = current_time
                server_3_restart()
            time.sleep(1)

def timer_thread_4():
    global last_reset_time_4
    if timer_running_4:
        print("timer thread 4 started")
        while True:
            current_time = time.time()
            if current_time - last_reset_time_4 >= time_to_check_servers:
                print("server 4 offline go to restart...")
                last_reset_time_4 = current_time
                server_4_restart()
            time.sleep(1)

def main():
    if server_1_enable == "True":
        if server_1_dir == "dir":
            print("Please insert the directory 1 server")
            return
    if server_2_enable == "True":
        if server_2_dir == "dir":
            print("Please insert the directory 2 server")
            return
    if server_3_enable == "True":
        if server_3_dir == "dir":
            print("Please insert the directory 3 server")
            return
    if server_4_enable == "True":
        if server_4_dir == "dir":
            print("Please insert the directory 4 server")
            return
    
    global last_reset_time_1
    global last_reset_time_2
    global last_reset_time_3
    global last_reset_time_4
    global timer_running_1
    global timer_running_2
    global timer_running_3
    global timer_running_4
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", Port))
    server_socket.listen(0)
    print(f"The server is listening on port: {Port}...")

    last_reset_time_1 = time.time()
    last_reset_time_2 = time.time()
    last_reset_time_3 = time.time()
    last_reset_time_4 = time.time()
    
    if server_1_enable != "False":
        timer_running_1 = True

    if server_2_enable != "False":
        timer_running_2 = True

    if server_3_enable != "False":
        timer_running_3 = True

    if server_4_enable != "False":
        timer_running_4 = True

    timer_1 = threading.Thread(target=timer_thread_1)
    timer_1.daemon = True
    timer_1.start()
    timer_2 = threading.Thread(target=timer_thread_2)
    timer_2.daemon = True
    timer_2.start()
    timer_3 = threading.Thread(target=timer_thread_3)
    timer_3.daemon = True
    timer_3.start()
    timer_4 = threading.Thread(target=timer_thread_4)
    timer_4.daemon = True
    timer_4.start()

    while True:
        client_socket, _ = server_socket.accept()
        data = client_socket.recv(1024)
        if not data:
            break
        decoded_data = data.decode('utf-8')
        if "1 True" in decoded_data:
            print("server 1 on")
            last_reset_time_1 = time.time()
        if "2 True" in decoded_data:
            print("server 2 on")
            last_reset_time_2 = time.time()
        if "3 True" in decoded_data:
            print("server 3 on")
            last_reset_time_3 = time.time()
        if "4 True" in decoded_data:
            print("server 4 on")
            last_reset_time_3 = time.time()

        client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()