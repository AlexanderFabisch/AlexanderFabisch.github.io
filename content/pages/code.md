Title: Software
Date: 2014-11-19 07:40
Category: Software

I am involved in some open source projects. Here are some of them. I also have
a [Github account](https://github.com/AlexanderFabisch).

<table style="border-spacing: 15px; border-collapse: separate;">
  <tbody>
    <tr>
      <td><img src="https://raw.githubusercontent.com/rock-learning/bolero/master/doc/source/_static/logo.png" width=200px /></td>
      <td style="vertical-align:top;">
        <a href="https://github.com/rock-learning/bolero">BOLeRo</a> - Behavior Optimization and Learning for Robots. (C++, Python)<br/>
        BOLeRo provides tools to learn behaviors for robots. It includes behavior representations as well as reinforcement learning, black-box optimization, evolutionary algorithms, and imitation learning. It provides a C++ and a Python interface to be efficient where this is required and to be flexible and convenient where performance is not an issue. Because the library provides a C++ interface, it is easy to integrate in most robotic frameworks, e.g. the robot operating system (ROS) or the robot construction kit (Rock).
      </td>
    </tr>
    <tr>
      <td><img src="https://rock-learning.github.io/pytransform/_images/rotations.svg" width=200px /></td>
      <td style="vertical-align:top;">
        <a href="https://github.com/rock-learning/pytransform">pytransform</a>
        - A tool for handling transformations (conversions, plotting, editing, ...) (Python)<br/>
        A Python library for transformations in three dimensions. It makes conversions between rotation and transformation conventions as easy as possible. The library focuses on readability and debugging, not on computational efficiency. If you want to have an efficient implementation of some function from the library you can easily extract the relevant code and implement it more efficiently in a language of your choice.
      </td>
    </tr>
    <tr>
      <td><img src="http://www.informatik.uni-bremen.de/~afabisch/files/openann-logo.png" width=200px /></td>
      <td style="vertical-align:top;">
        <a href="https://github.com/OpenANN/OpenANN">OpenANN</a>
        - A library for artificial neural networks. (C++, Python)<br/>
        OpenANN is an open source library for artificial neural networks. It is open for users that want to apply ANN to their problems, developers and researchers that want to implement new technologies and students that want to understand the tricks that are required to implement neural networks. It follows a minimal dependency policy, i.e. we rely on only a few libraries and tools. It is not designed to use the full potential of GPUs though, but it is possible to run it on very limited systems, e.g. robotic platforms.</td>
    </tr>
    <tr>
      <td style="vertical-align:top;">
        <img src="https://raw.githubusercontent.com/AlexanderFabisch/gmr/master/gmr.png" width=200px /></td>
      <td><a href="https://github.com/AlexanderFabisch/gmr">gmr</a>
        - An implementation of Gaussian mixture models for clustering and regression. (Python)<br/>
        There is an implementation of Gaussian Mixture Models for clustering in scikit-learn as well. Regression could not be easily integrated in the interface of sklearn. That is the reason why I put the code in a separate repository.
      </td>
    </tr>
    <tr>
      <td><img src="https://upload.wikimedia.org/wikipedia/commons/d/d8/Concept_of_directional_optimization_in_CMA-ES_algorithm.png" width=200px /></td>
      <td style="vertical-align:top;"><a href="https://github.com/AlexanderFabisch/CMA-ESpp">CMA-ESpp</a>
        - Implementation of the derivative-free optimization algorithm CMA-ES. (C++)<br/>
        The code is based on Hansen's ANSI C implementation of CMA-ES.
      </td>
    </tr>
    <tr>
      <td><img src="https://raw.githubusercontent.com/AlexanderFabisch/slither/master/slither.png" width=200px /></td>
      <td style="vertical-align:top;"><a href="https://github.com/AlexanderFabisch/slither">slither</a>
        - A private replacement for online training logs. (Python)<br/>
        Commercial services that allow you to record your sport activities store your data on some server which you cannot control. You do not know what they use the data for and you cannot write your own tools to analyze your own data. slither tries to change that by replacing online services. It allows you to store your training sessions (in .tcx format) and analyze them on your computer.
      </td>
    </tr>
    <tr>
      <td><img src="http://www.informatik.uni-bremen.de/~afabisch/files/cythonwrapper.png" width=200px /></td>
      <td style="vertical-align:top;"><a href="https://github.com/AlexanderFabisch/cythonwrapper">cythonwrapper</a>
        - Automatically generates a Cython wrapper for C++ code. (Python, Cython)<br/>
        This tool is able to parse C++ headers and automatically generate Python bindings from it. It makes use of Clang for parsing and Cython for to build the extension.
      </td>
    </tr>
  </tbody>
</table>
