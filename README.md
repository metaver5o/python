# python

- I´ve created this repo in order to study Python language.
- Following all exercises from http://learnpythonthehardway.org/
- any regards please share to python@corp.mmatos.com


## this is how I setup my docker env in order to test the exercises:
# mkdir /opt/code/; ln -s /code ~/code/
# cd ~/code/; git clone your.python.git.repo.comes.here
# docker pull python:2.7
# docker run -ti --name py -v /opt/code/:/opt/code/ python:2.7
# docker exec py python /opt/code/repo/file.py 
# docker attach py #run your py 
