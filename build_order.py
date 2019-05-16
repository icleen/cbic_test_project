import os, sys


def read_input(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f if len(line) > 1 and line[0] != '#']
    assert len(lines)%2 == 0
    projs = None
    insts = []
    for i, line in enumerate(lines):
        if i%2 == 0:
            assert 'projects' in line
            projs = line.split('projects:')[-1].strip()
            projs = projs.split(', ')
        else:
            assert 'dependencies' in line
            deps = line.split('dependencies:')[-1].strip()
            deps = deps.split('), (')
            deps = [dep.strip('()').split(', ', 2) for dep in deps]
            insts.append( (projs, deps) )

    return insts


def find_build_order(projs, deps):
    buildo = []
    last = len(buildo)
    while len(projs) > 0:
        # print(projs)
        # print(deps)
        # print(buildo)
        # input('...')
        depchart = {}
        for p in projs:
            depchart[p] = False
            for d in deps:
                depchart[p] += (p == d[1])
        projs = []
        for key in depchart:
            if depchart[key]:
                projs.append(key)
            else:
                buildo.append(key)
                deps = [d for d in deps if d[0] != key]
        if len(buildo) <= last:
            return 'No valid build order!!!'
        last = len(buildo)
    return buildo


def find_build_order2(projs, deps):
    buildo = []
    last = len(buildo)
    depchart = {}
    for p in projs:
        depchart[p] = []
        for d in deps:
            if p == d[1]:
                depchart[p].append(d[0])
    while len(projs) > len(buildo):
        # print(depchart)
        # print(buildo)
        # input('...')
        for key in depchart:
            if len(depchart[key]) < 1 and key not in buildo:
                buildo.append(key)
                for key2 in depchart:
                    depchart[key2] = [val for val in depchart[key2] if val != key]
        if len(buildo) <= last:
            return 'No valid build order!!!'
        last = len(buildo)
    return buildo


def main():
    deps_file = "deps_test1.txt"
    dep_projs = read_input(deps_file)
    for dp in dep_projs:
        # buildo = find_build_order(*dp)
        # print('final buildo:', buildo)
        buildo = find_build_order2(*dp)
        print('final build order:', buildo)
        # input('...')

if __name__ == '__main__':
    main()
