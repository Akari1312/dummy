import subprocess

# insecure command execution

def run_ping(host):
    # potential command injection if host is from user input
    command = f"ping -c 4 {host}"
    result = subprocess.check_output(command, shell=True, text=True)
    return result
