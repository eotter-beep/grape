import subprocess
import sys
import os
import time

def stop_audio_drivers():
    # Stop PulseAudio
    print("Stopping PulseAudio...")
    subprocess.run(["systemctl", "--user", "stop", "pulseaudio.service"], check=False)
    subprocess.run(["systemctl", "--user", "stop", "pulseaudio.socket"], check=False)
    
    # Stop PipeWire
    print("Stopping PipeWire...")
    subprocess.run(["systemctl", "--user", "stop", "pipewire.service"], check=False)
    subprocess.run(["systemctl", "--user", "stop", "pipewire.socket"], check=False)
    subprocess.run(["systemctl", "--user", "stop", "pipewire-pulse.service"], check=False)
    
    print("Audio drivers stopped.")
    time.sleep(2)  # Give some time for drivers to fully stop

def start_driver(driver_path="driver.py"):
    if not os.path.isfile(driver_path):
        print(f"Driver file {driver_path} not found!")
        sys.exit(1)
    print(f"Starting driver: {driver_path}")
    subprocess.run([sys.executable, driver_path])

if __name__ == "__main__":
    stop_audio_drivers()
    start_driver("driver.py")
