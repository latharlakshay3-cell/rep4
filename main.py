import subprocess
import os

def main():
    ip = os.getenv("IP")
    port = os.getenv("PORT_TARGET")
    duration = os.getenv("TIME")
    size = os.getenv("PACKET_SIZE")
    threads = os.getenv("THREADS")

    if not all([ip, port, duration, size, threads]):
        print("Missing environment variables")
        return

    if os.path.exists("mrx"):
        os.chmod("mrx", 0o755)

    print(f"Starting process on {ip}:{port}")

    subprocess.run(
        ["./mrx", ip, port, duration, size, threads]
    )

    print("Process finished")

if __name__ == "__main__":
    main()
