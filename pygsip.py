import socket
from colorama import init, Fore



init()

print(Fore.LIGHTGREEN_EX + """████─██─██─████─███─███─████
█──█──███──█────█────█──█──█
████───█───█─██─███──█──████
█──────█───█──█───█──█──█───
█──────█───████─███─███─█───""")

print("Commands: \nstart\nexit")

def deff():
    def get_ip_by_hostname():
        hostname = input("Please enter a website address(URL): ")

        try:
            return f'Hostname: {hostname}\nIP address: {socket.gethostbyname(hostname)}'
        except socket.gaierror as error:
            return f'Invalid Hostname - {error}'
        
    def main():
        print(Fore.RED+get_ip_by_hostname())
        #file = open("ip.txt", "w")
        #file.write(get_ip_by_hostname())

    if __name__ == '__main__':
        main()

while True:
    comm = input(Fore.RESET+Fore.LIGHTGREEN_EX+"Command: ")
    if comm == "start":
        deff()
    if comm == "exit":
        y_n = input("Do you want exit? y/n ")
        if y_n == "y":
            print(Fore.RESET + "Program Closed!")
            break
        else:
            pass
    
    pass