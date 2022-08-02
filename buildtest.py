#!/usr/bin/python3

build_variants = [
    'WITH_ADNS',
    'WITH_BRIDGE',
    'WITH_CJSON',
    'WITH_DOCS',
    'WITH_EC',
    'WITH_EPOLL',
    'WITH_MEMORY_TRACKING',
    'WITH_PERSISTENCE',
    'WITH_SHARED_LIBRARIES',
    'WITH_SOCKS',
    'WITH_SRV',
    'WITH_STATIC_LIBRARIES',
    'WITH_STRIP',
    'WITH_SYSTEMD',
    'WITH_SYS_TREE',
    'WITH_THREADING',
    'WITH_TLS',
    'WITH_TLS_PSK',
    'WITH_UNIX_SOCKETS',
    'WITH_WEBSOCKETS',
    'WITH_WRAP',
    'WITH_XTREPORT',
]

special_variants = [
    'WITH_BUNDLED_DEPS',
    'WITH_COVERAGE',
]


import os
import random
import subprocess

def run_test(msg, opts):
    subprocess.run(["make", "clean"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"{msg}: {str(opts)}")
    args = ["make", "-j%d" % (os.cpu_count())] + opts
    proc = subprocess.run(args, stdout=subprocess.DEVNULL)
    if proc.returncode != 0:
        raise RuntimeError(f"BUILD FAILED: {' '.join(args)}")

def simple_tests():
    for bv in build_variants:
        for enabled in ["yes", "no"]:
            opts = f"{bv}={enabled}"
            run_test("SIMPLE BUILD", [opts])

def random_tests(count=10):
    for _ in range(1, count):
        opts = [f'{bv}={random.choice(["yes", "no"])}' for bv in build_variants]
        run_test("RANDOM BUILD", opts)


if __name__ == "__main__":
    simple_tests()
    random_tests(100)
