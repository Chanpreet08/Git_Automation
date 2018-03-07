#!/bin/bash



if [ $# -eq 0 ]
	then
		echo 'No argument provided'
	else 
		commit_message=$1
		
		tags=($(git tag))

		latest_tag=${tags[-1]}

		curr_ver=${latest_tag:1:3}

		new_ver=$(echo "$curr_ver + 0.1"|bc -l)

		new_tag='v'$new_ver

		git status 

		git add .

		git commit -m "$commit_message"

		git status 

		git tag $new_tag

		git push origin $new_tag
fi