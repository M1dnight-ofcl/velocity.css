import shutil, os
version = 0.1
print(f"""
- ~{{[ VELOCITY PACKAGE BUILDER ]}}~ - 
        M1dnightDev (c) 2023
            Version {version}
""")
# note: x-x-x preferred but x.x.x will work and be converted to x-x-x
versionName = input("Please input the version name of this release: ")
versionName = versionName.lower().replace(".", "-")

versionReleaseType = input("Please input the type of this release: ")
versionReleaseType = f"{versionReleaseType.lower()}"

velocityPath = f'{os.getcwd()}/velocity/style/'
releaseDirectory = f'{os.getcwd()}/release/'

if not os.path.exists(releaseDirectory):
    os.mkdir(releaseDirectory)

shutil.make_archive(f"release/velocity.{versionReleaseType}.{versionName}", 'zip', velocityPath)

print(f'\nscript completed with exit 0\nyour file can be found at {os.getcwd()}\\release\\velocity.{versionReleaseType}.{versionName}.zip')
