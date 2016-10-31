# Circular times tables
Geometric series plotted on a circle instead of a straight line create beautiful and often unintuitive patterns. Some of the more basic patterns are known as [cardioids](https://en.wikipedia.org/wiki/Cardioid) and nephroids and appear in both the physical and the abstract world, like sun rays reflected [in a coffee cup](https://en.wikipedia.org/wiki/Cardioid#/media/File:Caustique.jpg) or the bulb of the Mandelbrot series.

This program visualizes such patterns with different parameters. There is a great introductory [clip](https://www.youtube.com/watch?v=qhbuKbxJsk8) here.

## 1. Dependencies
* Python v2
* matplotlib

## 2. Preparation

1. Download and extract the [code](https://github.com/antonfjodorov/circular-timestables)
2. Install the dependencies, easiest using [pip](https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip)
3. Install Python library matplotlib

Example on Linux

```
$ apt-get install python
$ apt-get install pip
$ pip install matplotlib
```

## 3. Run

Run the program, using for example base 60:

`$ python circular-times-tables.py -b 60`

![](http://oi68.tinypic.com/2ywiykj.jpg)

The following results in multiple graphs, using bases 12 to 16 and multiplying factor 3.

`$ python circular-times-tables.py -b 12 -B 16 -m 3`

## 4. Alternative algorithm: Fibonacci
The core of the program is $${c_n = m*c_{n-1}}$$ which means that the next line depends on the previous geometrically. What if this dependence were Fibonacci-based? $${c_n = c_{n-1}+c_{n-2}}$$

Corresponding changes to the code:
```python
def _drawLines(self):
	a = 1
	b = 1
	for i in xrange(1,5*self.N+1):
		c = a + b
		a = b
		b = c
		...
```


Turns out, there are many different patterns. One of the simpler ones look like a base tower (base 14 and base 35).
![](http://i66.tinypic.com/15y6i4h.jpg)
Fibonacci, base 14
![](http://i68.tinypic.com/122lroy.png)
Fibonacci, base 35

And there are more complex patterns, like base 26 and base 51.
![](http://i64.tinypic.com/24dewau.png)
Fibonacci, base 26
![](http://i63.tinypic.com/s1qis6.png)
Fibonacci, base 51

## License
MIT

