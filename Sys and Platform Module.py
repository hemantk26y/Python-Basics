# WAP to get familiarize with sys and platform module

import sys
import platform
print("Python version")
print(sys.version)
print("================================================================================")
print("System info.")
print(sys.version_info)
print(f"Computer network name: {platform.node()}")
print(f"Machine type: {platform.machine()}")
print(f"Processor type: {platform.processor()}")
print(f"Platform type: {platform.platform()}")
print(f"Operating system: {platform.system()}")
print(f"Operating system release: {platform.release()}")
print(f"Operating system version: {platform.version()}")
