from pathlib import Path
import random

INPUT_LIMIT = 100_000

SAMPLES = [
["""11 20
2 5 3 7 2 1 10 4 1 8 2
1 2 2 2 5 5 1 8 8 8""", "Basic test case; no unreachable nodes."],
["""5 7
1 5 10 -2 -2
1 1 3 3""", "Basic tree case; using negative weights, exceeding weight subtree."],
["""5 7
8 5 10 -2 -2
1 1 3 3""", "No reachable children, bottleneck at root; single coach needed."]
]

for sample, (test_case, description) in enumerate(SAMPLES, 1):
    filename = f"sample{sample}"

    Path(filename + ".in").write_text(test_case)
    Path(filename + ".desc").write_text(description)


def write_testcase(filename, test_case, description):
    Path(filename + ".in").write_text(test_case)
    Path(filename + ".desc").write_text(description)


def single_parent_single_child():
    test_case = (
        "2 20\n"
        "10 10\n"
        "1"
    )
    write_testcase("single_parent_single_child", test_case, "Two nodes, with a single child, each being reachable. The child is reachable, but is directly on the barrier.")


def negative_root_node_weight():
    test_case = (
        "5 10\n"
        "-100 90 100 110 120\n"
        "1 1 1 1"
    )
    write_testcase("negative_root_node_weight", test_case, "Root has negative weight and children are partially reachable.")


def binary_tree_two_layers():
    test_case = (
        "7 10\n"
        "5 5 5 1 1 1 1\n"
        "1 1 3 3 2 2"
    )
    write_testcase("binary_tree_two_layers", test_case, "Binary tree of 3 layers with unreachable third layer.")


def unreachable_subtree_with_negatives():
    test_case = (
        "11 20\n"
        "1 3 7 -2 2 -6 1 30 3 5 5\n"
        "1 1 1 3 3 3 4 4 8 8"
    )
    write_testcase("unreachable_subtree_with_negatives", test_case, "Unreachable subtree in a tree including negative weights.")


def exponential_weights():
    test_case = (
        "14 15\n"
        "1 2 2 2 4 4 4 4 8 8 8 8 16 16\n"
        "1 1 1 3 3 4 4 6 6 8 8 10 10"
    )
    write_testcase("exponential_weights", test_case, "Exponentially increasing weights of simple tree.")


def single_node_bottleneck():
    test_case = (
        "6 5\n"
        "1 10 -8 -8 -8 -8\n"
        "1 2 2 2 2"
    )
    write_testcase("single_node_bottleneck", test_case, "There is a single bottleneck in the tree, which renders all its children unreachable.")

def large_increasing_path():
    test_case = ""

    employees = INPUT_LIMIT
    threshold = INPUT_LIMIT // 2
    test_case += f"{employees} {threshold}\n"

    test_case += ("1 " * employees).strip() + "\n"

    test_case += " ".join(str(x) for x in range(1, employees))

    write_testcase("large_increasing_path", test_case, "A long path (only single child per node), where each child was weight 1.")


def switching_path():
    test_case = ""

    employees = 1_000
    threshold = 1
    test_case += f"{employees} {threshold}\n"

    test_case += ("1 -1 " * (employees // 2) + "1" * (employees % 2)).strip() + "\n"

    test_case += " ".join(str(x) for x in range(1, employees)) + "\n"

    write_testcase("switching_path", test_case, "Long path of nodes. Each node has either weight 1 or -1. No path length is larger 1.")


def negative_only_test():
    test_case = ""

    hierarchical_levels = 8
    employees = 0
    for level in range(0, hierarchical_levels):
        employees += 3**level

    threshold = 20
    test_case += f"{employees} {threshold}\n"

    # Each person has negative motivational level
    test_case += " ".join(str(-x) for x in range(employees)) + "\n"

    test_case += " ".join(f"{x} {x} {x}" for x in range(1, employees//3)) + "\n"

    write_testcase("negative_only", test_case, "Ternary tree with negative weights only. All nodes reachable.")


def random_test_case(case_number, input_size, type):
    test_case = ""

    employees = input_size
    threshold = random.randint(1, employees // 10)

    test_case += f"{employees} {threshold}\n"
    test_case += " ".join(str(random.randint(-threshold, threshold)) for x in range(employees)) + "\n"

    bosses = [1]
    for i in range(2, employees):
        boss = random.randint(1, i-1)
        bosses.append(boss)
    test_case += " ".join([str(x) for x in bosses]) + "\n"

    write_testcase(f"random_test_case_{case_number}_{type}", test_case, f"Randomly generated tree: test case #{case_number}; n={employees}, threshold={threshold}, type={type}")
    

# ------------------------
# Small Test Cases
# ------------------------

# Relatively simple trees
binary_tree_two_layers()
unreachable_subtree_with_negatives()
exponential_weights()
single_node_bottleneck()
single_parent_single_child()
negative_root_node_weight()

# ------------------------
# Large Test Cases
# ------------------------

# path test cases: Tree, where each node has only one child
large_increasing_path()
switching_path()

# Each node has three children and each motivational level of -1
negative_only_test()

# Random test cases
# Limit Tests
for i in range(1, 6):
    random_test_case(i, random.randint(500, 10_000), "small")
for i in range(6, 10):
    random_test_case(i, INPUT_LIMIT, "large")
