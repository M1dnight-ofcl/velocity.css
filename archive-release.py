import shutil, os
version = 0.1
print(f"""
- ~{{[ VELOCITY PACKAGE BUILDER ]}}~ - 
        M1dnightDev (c) 2023
            Version {version}
""")
# note: x-x-x preferred but x.x.x will work and be converted to x-x-x
versionName = input("Please input the version name of this release: ")
versionName.lower().replace(".", "-")

versionReleaseType = input("Please input the type of this release: ")
versionReleaseType = f"{versionReleaseType.lower()}"

velocityPath = os.getcwd() + 'velocity/style/'

shutil.make_archive(f"velocity.{versionReleaseType}.{versionName}", 'zip', velocityPath)

print(f'\nscript complete\nyour file can be found at {os.getcwd()}\\velocity.{versionReleaseType}.{versionName}.zip')
