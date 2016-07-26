# gomake-telemetry

goMake Telemetry System

## Getting Started

### Requirements

* Python 2.7+

### Installation

Setup environment variables (see examples in __main__.py for guidance):

```
DB_PATH=/path/to/sqlite/file
LOG_PATH=/path/to/writeable/logfile
GPS_PATH=/dev/tty[NameOfSerialDevice]
GPS_BAUD=4800
SAT_PATH=/dev/tty[NameOfSerialDevice]
SAT_BAUD=19200
PID_PATH=/path/to/writeable/pid/file
```

Install gomake-telemetry:

```
$ git clone https://github.com/jonathanbarton/gomake-telemetry.git
```

## Basic Usage

After installation, the package can imported:

```
$ cd gomake-telemetry
$ python .
```

## Documentation

Read the full documentation [here](http://jonathanbarton.github.io/gomake-telemetry).
