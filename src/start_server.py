import subprocess
import sys
import pkg_resources

REQUIRED_PACKAGES = [
    "mcp>=1.0.0",
]

def install_packages(packages):
    """Installs the given packages using pip."""
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")
            sys.exit(1)

def check_and_install_dependencies():
    """Checks for required packages and installs them if they are missing."""
    missing_packages = []
    for package in REQUIRED_PACKAGES:
        try:
            pkg_resources.require(package)
        except (pkg_resources.DistributionNotFound, pkg_resources.VersionConflict):
            missing_packages.append(package)

    if missing_packages:
        print(f"Missing packages: {', '.join(missing_packages)}. Installing...")
        install_packages(missing_packages)
        print("Dependencies installed successfully.")

if __name__ == "__main__":
    check_and_install_dependencies()
    # Now that dependencies are installed, start the main server
    from server import main
    main()
