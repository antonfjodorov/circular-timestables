# Circular times tables
Geometric series plotted on a circle instead of a straight line create beautiful and often unintuitive patterns. Some of the more basic patterns are known as [cardioids](https://en.wikipedia.org/wiki/Cardioid) and nephroids and appear in both the physical and the abstract world, like sun rays reflected [in a coffee cup](https://en.wikipedia.org/wiki/Cardioid#/media/File:Caustique.jpg) or the bulb of the Mandelbrot series.

This program visualizes such patterns with different parameters. There is a great introductory [clip](https://www.youtube.com/watch?v=qhbuKbxJsk8) here.

## Dependencies
* Python v2
* matplotlib

## Preparation

1. Download and extract the [code](https://github.com/antonfjodorov/circular-timestables)
2. Install the dependencies, easiest using [pip](https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip)
3. Install Python library matplotlib

Example on Linux

```
$ apt-get install python
$ apt-get install pip
$ pip install matplotlib
```

## Run

Run the program, using for example base 60:

`$ python circular-times-tables.py -b 60`

![](http://oi68.tinypic.com/2ywiykj.jpg)

The following results in multiple graphs, using bases 12 to 16 and multiplying factor 3.

`$ python circular-times-tables.py -b 12 -B 16 -m 3`

## License
MIT
