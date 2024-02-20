#!/usr/bin/env bash

# This script compiles all requirements.in files to requirements.txt files
# This means that all dependencies are locked to a specific version
# Plus, it checks if the requirements.in file has changed since the last time it was compiled
# If not, it skips the file rather than recompiling it (which may change version unnecessarily often)

if ! command -v uv &> /dev/null; then
	echo "uv is not installed. Please run pip3 install --user uv" >&2
	exit 1
fi

script_dir=$(dirname "$(realpath -s "$0")")
# NOTE: sha256sum will put the file path in the hash file.
# To simplify the directory (using relative paths), we change the working directory.
cd "$script_dir/../deps" || exit 1

shopt -s globstar
num_files=0
num_up_to_date=0
for file in requirements*.in; do
	# $file: requirements.in
	((num_files++))

	lockfile="${file%.in}.txt"  # requirements.txt
	shafile=".$file.sha256"  # .requirements.in.sha256
	# Process only changed files by comparing hash
	if [[ -f "$lockfile" ]] && [[ -f "$shafile" ]]; then
		if sha256sum -c "$shafile" &> /dev/null; then
			echo "Skipping $file due to no changes"
			((num_up_to_date++))
			continue
		fi
	fi
	echo "Generating lockfile $lockfile from $file"
    uv pip compile "$file" -o "$lockfile"
	sha256sum "$file" > "$shafile"  # update hash
done

# exit code 2 when all files are up to date
if [[ $num_files -eq $num_up_to_date ]]; then
	echo "All files are up to date!"
	exit 2
fi
