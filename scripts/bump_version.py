import toml

# Load pyproject.toml
with open("pyproject.toml", "r") as f:
    pyproject = toml.load(f)

# Get current version
version = pyproject["project"]["version"]
major, minor, patch = map(int, version.split("."))
patch += 1
new_version = f"{major}.{minor}.{patch}"

# Update version
pyproject["project"]["version"] = new_version

# Save back
with open("pyproject.toml", "w") as f:
    toml.dump(pyproject, f)