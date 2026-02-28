import subprocess

# insecure command execution in notification helper

def run_notification(user):
    # potential command injection if user input is not sanitized
    command = f"echo Sending reminder to {user}"
    result = subprocess.check_output(command, shell=True, text=True)
    return result
