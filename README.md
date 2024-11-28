This is a modular and scalable pipline

This pipline is composed out of 4 modules:
  1. Loade
  2. Cleaner
  3. Processor
  4. Exporter

Every module is implemented by a class which inherit from an abstract class.

All necessary directories exist in repo including a parameters yaml file
pathes can be changed in the yaml file

Version:
python - 3.10.4
pandas - 2.2.3

Things I haven't managed to complete:
1. Try except are not wrapping all modules (most important Exporter)
2. columns dtypes should be set from yaml as well
3. Logging is implemeted only for Loader
4. Not all classes and functions are well documented, I tryed to give every thing a self explainatory name
5. I didnt have time to check every thing so i guess there are minor mistakes and inconsistencies.

HAVE FUN :)
