# Python Software Engineering Examples

A practical collection of small Python examples for learning software engineering
concepts step by step — from zero to advanced.

The repository follows a learning path: Python fundamentals, functions, classes,
data structures, OOP, SOLID, design patterns, system design, concurrency, and
advanced topics.

Each example is intentionally small and self-contained so it can be read, run,
and modified without needing a full application setup.

## Repository Structure

```text
PSE_000_Python_Basics/       Variables, types, loops, strings, lists, dicts, tuples
PSE_010_Input_Output/        stdin, file I/O, CSV, JSON, pathlib
PSE_020_Modules/             Imports, packages, pip, __name__
PSE_030_Functions/           Basics, args/kwargs, lambda, closures, decorators
PSE_040_Classes/             Attributes, access control, dataclasses
PSE_050_Error_Handling/      try/except, custom exceptions, best practices
PSE_060_Data_Structures/     Lists, dicts, sets, stacks, queues, trees, graphs
PSE_070_OOP/                 13 core OOP concepts
PSE_080_SOLID/               5 SOLID principles with examples
PSE_090_Design_Patterns/     23 GoF + 4 enterprise patterns
PSE_100_System_Design/       15 distributed systems topics
PSE_200_Concurrency/         Threads, multiprocessing, async/await
PSE_300_Advanced_Patterns/   Repository, DI, Unit of Work, Event Sourcing
```

Folder names use this convention:

```text
PSE_<NUMBER>_<TOPIC_NAME>
```

`PSE` means Python Software Engineering. Numbers follow a learning path from
000 (beginner) to 300 (expert), with gaps for future expansion.

## Learning Path (000 → 300)

| Level | Folder | Topic | What You Learn |
|-------|--------|-------|----------------|
| 000 | PSE_000 | Python Basics | Variables, types, control flow, collections |
| 010 | PSE_010 | Input / Output | stdin, files, CSV, JSON, pathlib |
| 020 | PSE_020 | Modules | Imports, packages, pip, \_\_name\_\_ |
| 030 | PSE_030 | Functions | Parameters, args/kwargs, lambda, closures, decorators |
| 040 | PSE_040 | Classes | Attributes, access control, dataclasses |
| 050 | PSE_050 | Error Handling | try/except, custom exceptions, best practices |
| 060 | PSE_060 | Data Structures | Lists, dicts, sets, stacks, queues, trees, graphs |
| 070 | PSE_070 | OOP | 13 core OOP concepts |
| 080 | PSE_080 | SOLID | 5 SOLID principles with examples |
| 090 | PSE_090 | Design Patterns | 23 GoF + 4 enterprise patterns |
| 100 | PSE_100 | System Design | 15 distributed systems topics |
| 200 | PSE_200 | Concurrency | Threads, multiprocessing, async/await |
| 300 | PSE_300 | Advanced Patterns | Repository, DI, Unit of Work, Event Sourcing |

## Topics Covered

### PSE_000 — Python Basics (8 files)

| # | File | Topic |
|---|------|-------|
| 1 | `PB_01_variables.py` | Variables, dynamic typing, unpacking |
| 2 | `PB_02_data_types.py` | int, float, str, bool, None |
| 3 | `PB_03_conditionals.py` | if / elif / else, ternary |
| 4 | `PB_04_loops.py` | for, while, enumerate, zip |
| 5 | `PB_06_strings.py` | String operations, formatting |
| 6 | `PB_07_lists.py` | Lists, slicing, comprehensions |
| 7 | `PB_08_dictionaries.py` | Dicts, comprehensions |
| 8 | `PB_09_tuples_sets.py` | Tuples, sets, frozenset |

### PSE_010 — Input / Output (1 file)

| # | File | Topic |
|---|------|-------|
| 1 | `IO_01_file_io.py` | stdin, file read/write, CSV, JSON, pathlib |

### PSE_020 — Modules (1 file)

| # | File | Topic |
|---|------|-------|
| 1 | `MDL_01_modules_and_packages.py` | Imports, stdlib, creating modules, \_\_name\_\_ |

### PSE_030 — Functions (6 files)

| # | File | Topic |
|---|------|-------|
| 1 | `01_basic_functions.py` | def, params, return, docstrings |
| 2 | `02_args_and_kwargs.py` | \*args, \*\*kwargs, combined signatures |
| 3 | `03_lambda_functions.py` | Lambdas, map, filter, sorted |
| 4 | `04_first_class_functions.py` | Passing and returning functions |
| 5 | `05_closures.py` | nonlocal, factory functions |
| 6 | `06_decorators.py` | @syntax, stacking, practical examples |

### PSE_040 — Classes (4 files)

| # | File | Topic |
|---|------|-------|
| 1 | `01_class_basics.py` | class, \_\_init\_\_, self, instance vs class attrs |
| 2 | `02_access_control.py` | public, protected (\_), private (\_\_) |
| 3 | `03_private_attributes.py` | Name mangling, double underscore |
| 4 | `04_dataclasses.py` | @dataclass, field, frozen |

### PSE_050 — Error Handling (1 file)

| # | File | Topic |
|---|------|-------|
| 1 | `EH_01_error_handling.py` | try/except, custom exceptions, chaining, best practices |

### PSE_060 — Data Structures (6 files)

| # | File | Topic |
|---|------|-------|
| 1 | `01_lists_and_arrays.py` | List as stack/queue, slicing, comprehensions |
| 2 | `02_dictionaries_as_maps.py` | defaultdict, Counter, nested dicts |
| 3 | `03_sets_and_relationships.py` | Union, intersection, frozenset |
| 4 | `04_stacks_and_queues.py` | LIFO/FIFO, deque, balanced parentheses, BFS |
| 5 | `05_trees.py` | TreeNode, BST, in/pre/post-order traversal |
| 6 | `06_graphs.py` | Adjacency list, BFS, DFS, path check |

### PSE_070 — OOP (13 files)

| # | Concept | File |
|---|---------|------|
| 01 | Encapsulation | `OOP_01_encapsulation.py` |
| 02 | Inheritance | `OOP_02_inheritance.py` |
| 03 | Polymorphism | `OOP_03_polymorphism.py` |
| 04 | Abstraction | `OOP_04_abstraction.py` |
| 05 | Composition | `OOP_05_composition.py` |
| 06 | Aggregation | `OOP_06_aggregation.py` |
| 07 | Association | `OOP_07_association.py` |
| 08 | Delegation | `OOP_08_delegation.py` |
| 09 | Abstract Class | `OOP_09_abstract_class.py` |
| 10 | Interface | `OOP_10_interface.py` |
| 11 | Duck Typing | `OOP_11_duck_typing.py` |
| 12 | Protocol | `OOP_12_protocol.py` |
| 13 | Mixin | `OOP_13_mixin.py` |

### PSE_080 — SOLID Principles (5 files)

| # | Principle | File |
|---|-----------|------|
| 01 | Single Responsibility | `SOLID_01_single_responsibility.py` |
| 02 | Open/Closed | `SOLID_02_open_closed.py` |
| 03 | Liskov Substitution | `SOLID_03_liskov_substitution.py` |
| 04 | Interface Segregation | `SOLID_04_interface_segregation.py` |
| 05 | Dependency Inversion | `SOLID_05_dependency_inversion.py` |

### PSE_090 — Design Patterns (27 files)

| Category | # | Pattern | File |
|---|---|---------|------|
| **Creational** | 1 | Singleton | `Creational/DP_C_01_singleton_pattern.py` |
| | 2 | Factory Method | `Creational/DP_C_02_factory_method_pattern.py` |
| | 3 | Abstract Factory | `Creational/DP_C_03_abstract_factory_pattern.py` |
| | 4 | Builder | `Creational/DP_C_04_builder_pattern.py` |
| | 5 | Prototype | `Creational/DP_C_05_prototype_pattern.py` |
| **Structural** | 1 | Facade | `Structural/DP_S_01_facade_pattern.py` |
| | 2 | Adapter | `Structural/DP_S_02_adapter_pattern.py` |
| | 3 | Decorator | `Structural/DP_S_03_decorator_pattern.py` |
| | 4 | Proxy | `Structural/DP_S_04_proxy_pattern.py` |
| | 5 | Composite | `Structural/DP_S_05_composite_pattern.py` |
| | 6 | Bridge | `Structural/DP_S_06_bridge_pattern.py` |
| | 7 | Flyweight | `Structural/DP_S_07_flyweight_pattern.py` |
| **Behavioral** | 1 | Strategy | `Behavioral/DP_B_01_strategy_pattern.py` |
| | 2 | Template Method | `Behavioral/DP_B_02_template_method_pattern.py` |
| | 3 | Observer | `Behavioral/DP_B_03_observer_pattern.py` |
| | 4 | Command | `Behavioral/DP_B_04_command_pattern.py` |
| | 5 | Chain of Responsibility | `Behavioral/DP_B_05_chain_of_responsibility_pattern.py` |
| | 6 | Iterator | `Behavioral/DP_B_06_iterator_pattern.py` |
| | 7 | State | `Behavioral/DP_B_07_state_pattern.py` |
| | 8 | Mediator | `Behavioral/DP_B_08_mediator_pattern.py` |
| | 9 | Visitor | `Behavioral/DP_B_09_visitor_pattern.py` |
| | 10 | Memento | `Behavioral/DP_B_10_memento_pattern.py` |
| | 11 | Interpreter | `Behavioral/DP_B_11_interpreter_pattern.py` |
| **Enterprise** | 1 | Repository | `Enterprise/AP_01_repository.py` |
| | 2 | Dependency Injection | `Enterprise/AP_02_dependency_injection.py` |
| | 3 | Unit of Work | `Enterprise/AP_03_unit_of_work.py` |
| | 4 | Event Sourcing | `Enterprise/AP_04_event_sourcing.py` |

All 23 classic Gang of Four patterns + 4 enterprise patterns.

### PSE_100 — System Design (15 files)

| # | File | Topic |
|---|------|-------|
| 1 | `01_client_service_model.py` | Client-server architecture |
| 2 | `02_http_rest.py` | HTTP methods, REST API design |
| 3 | `03_dns_and_load_balancing.py` | DNS, load balancing, GeoDNS |
| 4 | `04_caching_system.py` | Cache-aside pattern, cache vs DB |
| 5 | `05_rate_limiting_system.py` | Token bucket, sliding window |
| 6 | `06_message_queue.py` | Pub/sub, task queues |
| 7 | `07_database_replication.py` | Primary-replica, read replicas |
| 8 | `08_microservices_architecture.py` | Service decomposition, API gateway |
| 9 | `09_consistent_hashing.py` | Hash rings, virtual nodes |
| 10 | `10_url_shortener.py` | Encoding, redirection, analytics |
| 11 | `11_pagination.py` | Offset, cursor-based, keyset |
| 12 | `12_database_indexing.py` | B-tree, composite indexes |
| 13 | `13_proxy_forward_reverse.py` | Forward proxy, reverse proxy |
| 14 | `14_database_sharding.py` | Horizontal partitioning, shard keys |
| 15 | `15_pub_sub_system.py` | Topics, subscribers, fan-out |

### PSE_200 — Concurrency (4 files)

| # | File | Topic |
|---|------|-------|
| 1 | `01_sync_vs_async.py` | Blocking vs non-blocking I/O |
| 2 | `02_threads.py` | threading, Lock, GIL, thread safety |
| 3 | `03_multiprocessing.py` | Process Pool, parallel CPU work |
| 4 | `04_async_await.py` | Coroutines, gather, queues, producer-consumer |

### PSE_300 — Advanced Patterns (4 files)

| # | File | Topic |
|---|------|-------|
| 1 | `01_testing.py` | unittest, pytest, test organization |
| 2 | `02_type_checking.py` | Type hints, Protocol, generics |
| 3 | `03_packaging.py` | pyproject.toml, uv, project layout |
| 4 | `04_logging.py` | Levels, handlers, RotatingFileHandler |

## How To Use

Run any example directly with Python:

```bash
python PSE_000_Python_Basics/PB_01_variables.py
python PSE_030_Functions/06_decorators.py
python PSE_060_Data_Structures/05_trees.py
python PSE_070_OOP/OOP_04_abstraction.py
python PSE_080_SOLID/SOLID_01_single_responsibility.py
python PSE_090_Design_Patterns/Creational/DP_C_01_singleton_pattern.py
python PSE_090_Design_Patterns/Enterprise/AP_04_event_sourcing.py
python PSE_100_System_Design/04_caching_system.py
python PSE_200_Concurrency/04_async_await.py
python PSE_300_Advanced_Patterns/01_testing.py
```

Most files include:

- a short explanation at the top
- a small implementation of the concept
- a `main()` function that demonstrates the behavior

The examples are educational simulations. System design examples use in-memory
data structures instead of real servers, databases, queues, or network calls so
the core idea stays easy to inspect.

## Requirements

The project uses only the Python standard library.

The current `pyproject.toml` requires:

```text
Python >= 3.14
```

Many examples may also work on earlier Python 3 versions, but the repository is
configured for Python 3.14 or newer.

## Notes

- This is a learning repo, not a production framework.
- Examples favor clarity over completeness.
- System design examples are simplified models of real-world architectures.
- Folder numbering is for learning order, not Python package naming.
- Number gaps (110-190, 210-290) are reserved for future topics.
- New topics should stay small, runnable, and focused on one concept.

## Contributing

Contributions and improvements are welcome. Good additions include:

- clearer explanations
- more focused examples
- missing design patterns
- additional system design topics
- small corrections or naming fixes

## License

This repository is provided for educational purposes. See [LICENSE](LICENSE) for
details.
