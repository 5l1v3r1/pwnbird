from buffers import buffers
from .vtypes import bof


def sanity_check_buffer(buffer: buffers.StackBuffer, binary):
    vulnerabilities = []
    vulnerabilities.extend(bof.BufferOverflow(buffer.usages, binary).vulnerabilities)
    return vulnerabilities
