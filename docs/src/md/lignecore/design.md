# Design

## Overview

## Design Goals

* In-process integration with Unity frontend: Unity frontend can use backend without inter-process communications
* Support for implementing multiple types of user interfaces (e.g. standalone Unity application, client-server type network game, etc)
* Thread-safe: backend can be used from multiple frontend processes

## Design Constraints

* Backend is implemented in C#, and compiled as .NET library
* Backend is implemented as a single-threaded application



```mermaid
  graph TD;
      A-->B;
      A-->C;
      B-->D;
      C-->D;
```
