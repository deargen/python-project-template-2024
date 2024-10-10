# NOTE: Use this to replace all strings in the project template with the new project name,
# then delete this file.

# python-project-template-2024 -> new-ml-project
github_repo_name=new-project

# ml_project -> new_module_name
module_name=new_project

# ml-project -> new-package-name
package_name=new-project

# ML_PROJECT -> NEW_ENVVAR_NAME
envvar_name=NEW_PROJECT

# Python Project Template -> New Project
doc_title="New Project"
doc_url='https://deargen-ai.gitlab.io/new-project-docs'


rg --files-with-matches -l python-project-template-2024 | xargs sed -i -e "s/python-project-template-2024/$github_repo_name/g"
rg --files-with-matches -l ml_project | xargs sed -i -e "s/ml_project/$module_name/g"
rg --files-with-matches -l ml-project | xargs sed -i -e "s/ml-project/$package_name/g"
rg --files-with-matches -l ML_PROJECT | xargs sed -i -e "s/ML_PROJECT/$envvar_name/g"
rg --files-with-matches -l "Python Project Template" | xargs sed -i -e "s/Python Project Template/$doc_title/g"
rg --files-with-matches -l 'https://deargen-ai.gitlab.io/python-project-template-docs' | xargs sed -i -e "s|https://deargen-ai.gitlab.io/python-project-template-docs|$doc_url|g"

mv src/ml_project src/$module_name
