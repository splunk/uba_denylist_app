import argparse
from iocbin.app import IOCbinServer

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-p", "--port", default=5000, help="Port to accept connections on", type=int
    )

    args = parser.parse_args()
    print(f"[-] args: {args}")

    iocbin_server = IOCbinServer(args.port)
    iocbin_server.run_iocbin_server()

if __name__ == "__main__":
    main()


