#!/bin/bash
TEXT="empty"
TEXT1="empty"



function href()
{
	echo "####### start href.py"
	python3 href.py
	echo "####### href.py done"
	echo -n "####### confirm? (y/n): "
	read doing
	case $doing in
		y)
			echo "####### Confirmed!"
		;;
		n)
			href
	esac
}

function tor()
{
	echo "####### start tor.py"
	python3 tor.py
	echo "####### tor.py done"
	echo -n "####### confirm? (y/n): "
	read doing
	case $doing in
		y)
			echo "####### Confirmed!"
		;;
		n)
			tor
	esac
}

function handler()
{
	echo "####### start handler.py"
	python3 handler.py
	echo "####### handler.py done"
	echo -n "####### confirm? (y/n): "
	read doing
	case $doing in
		y)
			echo "####### Confirmed!"
		;;
		n)
			handler
	esac
}

function nz()
{
	echo "####### start nz.py"
	python3 nz.py
	echo "####### nz.py done"
	echo -n "####### confirm? (y/n): "
	read doing
	case $doing in
		y)
			echo "####### Confirmed!"
		;;
		n)
			nz
	esac
}

function full_poss()
{
	echo "####### start full_poss.py"
	python3 full_poss.py
	echo "####### full_poss.py done"
	echo -n "####### confirm? (y/n): "
	read doing
	case $doing in
		y)
			echo "####### Confirmed!"
		;;
		n)
			full_poss
	esac
}

function cov()
{
	echo "####### start cov.py"
	python3 cov.py
	echo "####### cov.py done"
	echo -n "####### confirm? (y/n): "
	read doing
	case $doing in
		y)
			echo "####### Confirmed!"
		;;
		n)
			cov
	esac
}




function exception()
{
	if [[ $TEXT != *"href.py"* ]]
		then
		href
	fi
	if [[ $TEXT != *"tor.py"* ]]
		then
		tor
	fi
	if [[ $TEXT != *"handler.py"* ]]
		then
		handler
	fi
	if [[ $TEXT != *"nz.py"* ]]
		then
		nz
	fi
	if [[ $TEXT != *"full_poss.py"* ]]
		then
		full_poss
	fi

	if [[ $TEXT != *"cov.py"* ]]
		then
		cov
	fi

}

function only()
{	
	if [[ $TEXT1 == *"href.py"* ]]
		then
		href
	fi
	if [[ $TEXT1 == *"tor.py"* ]]
		then
		tor
	fi
	if [[ $TEXT1 == *"handler.py"* ]]
		then
		handler
	fi
	if [[ $TEXT1 == *"nz.py"* ]]
		then
		nz
	fi
	if [[ $TEXT1 == *"full_poss.py"* ]]
		then
		full_poss
	fi
	if [[ $TEXT1 == *"cov.py"* ]]
		then
		cov
	fi

}


while getopts ":e:o:" opt ;
do
	case $opt in
		e)
			TEXT=$OPTARG
			exception

		;;
		o)
			TEXT1=$OPTARG
			only

	esac
done


if [ $TEXT1 == "empty" ] && [ $TEXT == "empty" ]
	then
	href
	tor
	handler
	nz
	full_poss
	cov
fi
