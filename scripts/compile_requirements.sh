#!/usr/bin/env bash

# This script compiles all requirements.in files to requirements.txt files
# This means that all dependencies are locked to a specific version
# Plus, it checks if the requirements.in file has changed since the last time it was compiled
# If not, it skips the file rather than recompiling it (which may change version unnecessarily often)

if ! command -v uv &> /dev/null; then
	echo "uv is not installed. Please run 'pip3 install --user uv'" >&2
	exit 1
fi

if ! command -v sha256sum &> /dev/null; then
	echo "sha256sum is not installed." >&2
	echo "If you're on Mac, run 'brew install coreutils'" >&2
	exit 1
fi

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# NOTE: sha256sum will put the file path in the hash file.
# To simplify the directory (using relative paths), we change the working directory.
cd "$SCRIPT_DIR/../deps" || { echo "Failure"; exit 1; }

if [[ $OSTYPE == "darwin"* ]]; then
	mkdir -p mac
fi

shopt -s globstar

function get_shafile() {
	local file=$1
	if [[ $OSTYPE == "darwin"* ]]; then
		echo "mac/.$file.sha256"
	else
		# .requirements.in.sha256
		echo ".$file.sha256"
	fi
}

function get_lockfile() {
	local file=$1
	if [[ $OSTYPE == "darwin"* ]]; then
		echo "mac/${file%.in}.txt"
	else
		# requirements.txt
		echo "${file%.in}.txt"
	fi
}

function file_content_changed() {
	# Check if the file has changed since the last time it was compiled, using the hash file.
	# NOTE: returns 0 if the file has changed
	local file=$1
	local shafile
	shafile=$(get_shafile "$file")
	if [[ -f "$shafile" ]] && sha256sum -c "$shafile" &> /dev/null; then
		return 1
	fi
	return 0
}


function deps_changed() {
	# Check if the requirements*.in file has changed since the last time it was compiled, including its dependencies (-r another_requirements.in).
	#
	# When the requirements have dependencies on other requirements files, we need to check if those have changed as well
	# e.g. requirements_dev.in has a dependency on requirements.in (-r requirements.in)
	# Note that we also need to recursively check if the dependencies of the dependencies have changed.
	# We need to recompile requirements_dev.txt if requirements.in has changed.
	# NOTE: returns 0 if the deps have changed
	local file=$1

	if file_content_changed "$file"; then
		return 0
	fi


	local file_deps
	file_deps=$(grep -Eo -- '-r [^ ]+' "$file")
	file_deps=${file_deps//"-r "/}  # remove -r
	for dep in $file_deps; do
		echo "ℹ️ $file depends on $dep"
		dep=${dep#-r }  # requirements.in
		if deps_changed "$dep"; then
			return 0
		fi
	done
	return 1
}

num_files=0
num_up_to_date=0
files_changed=()

# First, collect all files that need to be compiled.
# We don't compile them yet, because it will mess up the hash comparison.
for file in requirements*.in; do
	# $file: requirements.in
	((num_files++))

	lockfile=$(get_lockfile "$file")
	shafile=$(get_shafile "$file")
	# Process only changed files by comparing hash
	if [[ -f "$lockfile" ]]; then
		if ! deps_changed "$file"; then
			echo "⚡ Skipping $file due to no changes"
			((num_up_to_date++))
			continue
		fi
	fi
	files_changed+=("$file")
done

for file in "${files_changed[@]}"; do
	lockfile=$(get_lockfile "$file")
	shafile=$(get_shafile "$file")
	echo "🔒 Generating lockfile $lockfile from $file"
    uv pip compile "$file" -o "$lockfile" > /dev/null
	sha256sum "$file" > "$shafile"  # update hash
done

# exit code 2 when all files are up to date
if [[ $num_files -eq $num_up_to_date ]]; then
	echo "💖 All files are up to date!"
	exit 2
fi
