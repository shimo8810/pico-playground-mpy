# Pico Playground by MicroPython

This code is used to check connections with various devices using MicroPython. For details, please refer to `readme.md` for each project.

## Connection Method

The connection with Raspberry Pi Pico is established using `mpremote`.

Please refer to the [official documentation](https://docs.micropython.org/en/latest/reference/mpremote.html) for basic usage.

### Basic Usage

Here is how to use `mpremote`. Basically, if you can connect, upload, run, and install, you should be able to do it somehow.

#### Connection

Please specify the device name with `connect` as in the following command.

```bash
mpremote connect /dev/ttyACM0
```

#### Installation

Please use `mip` to install packages.

```bash
mpremote mip install iperf3
```

#### Upload

Please use the `fs cp` command to upload files to Raspberry Pi Pico. For example, copy it with a command like the following.

```bash
mpremote fs cp main.py :
```

#### Execution

If there is a `main.py` in the device, this file will be executed. If you want to execute a file locally, please run a command like the following.

```bash
mpremote run main.py
```
