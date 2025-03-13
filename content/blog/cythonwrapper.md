Title: Generating Python Bindings
Date: 2017-11-26 21:00
Category: Blog
Summary: I wrote a tool to generate Cython wrappers for C++ code that I presented in this article.

I often write C++ code and I often use Python. I usually want to use my C++ code in Python.
There are many tools that simplify the work of writing Python bindings ([Cython](http://docs.cython.org/en/latest/src/tutorial/clibraries.html), [SWIG](http://www.swig.org/), [Boost.Python](https://wiki.python.org/moin/boost.python), [pybind11](https://github.com/wjakob/pybind11), [CLIF](https://github.com/google/clif), ...). I personally like Cython. Most C++ features can be translated directly to Python with it.

Generating Python bindings for existing C++ libraries is usually a lot of manual work in Cython. Often conversions of custom data types (classes, structs) and memory management are difficult. Some features cannot even ever be translated to Python automatically or at all, for example:

* Templates: we cannot generate Python bindings for arbitrary types, even though Python is a dynamically typed language, bindings will usually be compiled and, hence, the template instantiation has to be known at compile time. You have to decide which template instantiations you need manually. This cannot be automized.
* Overloading: Python does not have the concept of overloading. As soon as you define two functions of the same name, the second definition will replace the first definition. The right way to do this in Python is to let a function examine its arguments and decide what to do with them.
* Combining multiple libraries and linking them cannot be automized.

## The Idea

Although not everything is easy, it still seems tedious to write glue code for very simple C++ classes like this one:
```
class A
{
public:
    double plus2(double d)
    {
        return d + 2.0;
    }
};
```
The good news is: we can automatically generate Python bindings for these simple cases. If all the relevant types are either [fundamental types](http://en.cppreference.com/w/cpp/language/types) (string, int, double, bool, ...) or defined in the library that you want to wrap. Clang can easily be used to build an abstract syntax tree from this header file. We can extract all interface definitions (classes, functions, etc.) and generate Python bindings with Cython. I implemented this idea in [cythonwrapper](https://github.com/AlexanderFabisch/cythonwrapper). It can be used as a command line tool, as a Python library or even as a Python import hook.

## How to Use It?

For the most simple use cases, you can use a command line tool. We can generate a Python extension that wraps a library defined in C++ header with:
```
pywrap <headers> --sources <sources> --modulename <name> --outdir <directory>
```
The result is located in the directory <directory> and can be build with:
```
python setup.py build_ext -i
```
If this is a header only library we can now simply do the following in Python:
```
from <name> import *
```
If we have to link a library, we will have to add that to the setup.py that has been generated.

If you have only a few lines of C++ code in a header file, there is even a much simpler solution that you can directly integrate in the Python code that uses the C++ code:
```
import pywrap.import_hook
import myheader
a = myheader.A()
b = 3.213
c = a.plus2(b)
```

If some configuration is required because the code is more complex, you can write a small script which uses the cythonwrapper library.

## Installation

Installation instructions are in the [readme](https://github.com/AlexanderFabisch/cythonwrapper#install).

## Features

What can we do with it?

### Comments

Clang automatically extracts documentation for classes, functions, etc. This documentation can be translated to Python docstrings automatically.
```
/**
 * This is a brief class description.
 *
 * And this is a detailed description.
 */
class MyClass
{
public:
    MyClass() {}
    /// Brief.
    void method() {}
};
```

In IPython you could print this information:

```
help(MyClass)
...
class MyClass(builtins.object):
 | This is a brief description.
 |
 | And this is a detailed description.
...
 | method(self)
 |     Brief.
...
```

### Operators

Both languages, C++ and Python support custom operators. They can automatically be translated from C++ to Python. All of the following operators can be translated to Python.

```
class Operators
{
public:
    Operators();
    int operator()(int a);
    int operator[](int a);
    int operator+(int a);
    int operator-(int a);
    int operator*(int a);
    int operator/(int a);
    int operator%(int a);
    bool operator&&(bool b);
    bool operator||(bool b);
    Operators& operator+=(int a);
    Operators& operator-=(int a);
    Operators& operator*=(int a);
    Operators& operator/=(int a);
    Operators& operator%=(int a);
    Operators& operator&=(bool b);
    Operators& operator|=(bool b);
};
```

### Custom Data Types

Custom data types that are defined in the files that will be parsed can automatically be used as function arguments and return values. For example, the class B which uses the previously defined class A from the following code can be wrapped automatically.

```
#include <string>


class A
{
    std::string s;
public:
    A();
    std::string getString() const;
};


class B
{
    const A& a;
public:
    B(const A& a);
    std::string getString();
};
```

Instead of a reference, you could also use a pointer. Note that since you are actually using C++, you have to make sure that you do not delete the object of class A that has been given to another object of class B if the object of class B still needs its reference to the object of type A.

### Inheritance

Inheritance can be handled automatically: all functions from its base classes are available in a class. For example, in the following hierarchy, class A also has the functions base1Method() and base2Method().

```
class Base1
{
public:
    virtual ~Base1();
    virtual int base1Method();
};

class Base2 : public Base1
{
public:
    virtual int base2Method();
};

class A : public Base2
{
public:
    virtual int aMethod();
};
```

### Templates

Templates have to be handled specially. You have to define which template instantiations should be wrapped in Python. Suppose we have a template function

```
template<typename T>
T addOne(T t)
{
    return t + T(1);
}
```

Here it makes sense to use the library directly to be able to configure the template specializations that will be available in Python:

```
from pywrap.defaultconfig import Config
from pywrap.cython import make_cython_wrapper, write_files


config = Config()
config.register_function_specialization(
    "addOne", "add_one_i", {"T": "int"})
config.register_function_specialization(
    "addOne", "add_one_d", {"T": "double"})

results = make_cython_wrapper(
    filenames=["template.hpp"], sources=[], config=config)
write_files(results, ".")
```

This will make the functions `add_one_i` and `add_one_d` available in Python.

```
In [1]: import template

In [2]: template.add_one_d(2.0)
Out[2]: 3.0

In [3]: template.add_one_i(2)
Out[3]: 3
```

### External Types

External types, e.g., Eigen matrices and vectors, can be used but it requires some manual work unfortunately. Here is a C++ example:

```
#include <Eigen/Core>


Eigen::VectorXd make(const Eigen::VectorXd& vector)
{
    return 2.0 * vector;
}
```

The configuration is too long to write it here, I'll just refer to the corresponding [unit test](https://github.com/AlexanderFabisch/cythonwrapper/blob/master/test/test_custom_conversions.py). We have to provide the C++ interface definition of an `Eigen::VectorXd` in Cython and we have to write a type converter from and to the corresponding Python type, in this case, a numpy array.

In the end, we can easily run this code:

```
from eigen import make
import numpy as np
a = np.ones(5)
b = make(a)
```

### Other Featurs

Some features have not been mentioned yet:

* STL exceptions are converted directly to the corresponding Python exceptions.
* Enums, structs, typedefs, static methods can be wrapped.
* STL templates, e.g., vectors, maps, etc. can be used as function arguments. (Not too deeply nested though...)

## Limitations

Code generation is usually only feasible if the library does not make extensive use of external types in the interface. My recommendation for these cases would be to write a simple C++ interface that will be wrapped in Python. A list of other issues can be found [in the readme](https://github.com/AlexanderFabisch/cythonwrapper#unsupported-features-of-c) but there are probably many more. For example, memory management: smart pointers are currently not supported automatically. You can do it manually though.

## Implementation Details

How does it work? Suppose we have a short C++ header:

```
typedef double mytype;


mytype fun(mytype d)
{
    return d + 1.0;
}
```

I use the [Python bindings of libclang](https://github.com/llvm-mirror/clang/blob/master/bindings/python/clang/cindex.py) to parse the header. If you increase verbosity, you will get the following output:

```
Node: CursorKind.TRANSLATION_UNIT, 'typedef.hpp.hpp'
  Node: CursorKind.TYPEDEF_DECL, 'mytype' (type: 'mytype')
  Node: CursorKind.FUNCTION_DECL, 'fun' (type: 'mytype (mytype)')
    Node: CursorKind.TYPE_REF, 'mytype' (type: 'mytype')
    Ignored node: CursorKind.TYPE_REF, mytype
    Node: CursorKind.PARM_DECL, 'd' (type: 'mytype')
      Node: CursorKind.TYPE_REF, 'mytype' (type: 'mytype')
      Ignored node: CursorKind.TYPE_REF, mytype
```

These are the information that Clang gives us. It is translated to another internal abstract syntax tree representation:
```
AST
    Typedef (double) mytype
    Function 'fun'
        Parameter (mytype) d
        Returns (mytype)
```

From this representation we can directly generate Cython code. That includes these files:

* _modulename.pxd - contains declarations corresponding to the C++ header
* modulename.pyx - defines the Python interface and contains the actual logic, for example, conversions between Python and C++ types
* setup.py - is required to build the Python extension

I use the template language [Jinja2](http://jinja.pocoo.org/docs/latest) to export these files. It really helps to separate layout and code in this application.

## Code

All the code is open source and available under New BSD license at [Github](https://github.com/AlexanderFabisch/cythonwrapper).
