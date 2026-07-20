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
PSE_000_Python_Basics/         Variables, types, loops, strings, lists, dicts, tuples, sets
PSE_010_Functions/             Basics, parameters, args/kwargs, lambda, closures, decorators
PSE_020_Builtins/              range, enumerate, zip, map, filter, sorted, any/all
PSE_030_Iterators_Generators/  Iterable, iterator, generator, yield
PSE_040_Input_Output/          stdin, print, file I/O, pathlib, serialization
PSE_050_Modules/               Imports, packages, venv, dependency management
PSE_060_Error_Handling/        Exceptions, custom exceptions, context managers
PSE_070_Classes/               Attributes, methods, properties, dataclasses
PSE_080_OOP/                   12 core OOP concepts
PSE_090_Data_Structures/       Stack, queue, linked list, heap, tree, graph
PSE_100_Type_Hints/            Basic typing, generics, protocols, type aliases
PSE_110_Concurrency/           CPU vs IO bound, threads, multiprocessing, asyncio
PSE_120_SOLID/                 5 SOLID principles with examples
PSE_130_Design_Patterns/       23 GoF + 1 behavioral patterns
PSE_135_Architectural_Patterns/ 5 enterprise architectural patterns
PSE_140_Testing/               unittest, pytest, mocking, fixtures
PSE_150_Standard_Library/      collections, itertools, functools, datetime, json, logging
PSE_160_System_Design/         17 distributed systems topics
PSE_170_Algorithms/            Big-O complexity, algorithm analysis
PSE_180_CLI_Frameworks/        argparse, click, typer
PSE_190_Serialization/         pydantic, orjson, yaml, toml, msgpack
PSE_200_Logging_Advanced/      structlog, loguru
PSE_210_HTTP_Client/           httpx, requests
PSE_220_Database/              SQLAlchemy ORM, sqlite3
PSE_230_Web_Frameworks/        FastAPI, Flask
PSE_240_Terminal_UI/           rich, textual
PSE_250_GUI/                   tkinter (standard library)
PSE_260_Packaging/             pyproject.toml, uv package manager
PSE_270_Capstone/              Full API server project
```

Folder names use this convention:

```text
PSE_<NUMBER>_<TOPIC_NAME>
```

`PSE` means Python Software Engineering. Numbers follow a learning path from
000 (beginner) to 270 (advanced).

## Learning Path (000 → 270)

| Level | Folder | Topic | What You Learn |
|-------|--------|-------|----------------|
| 000 | PSE_000 | Python Basics | Variables, types, control flow, collections |
| 010 | PSE_010 | Functions | Parameters, return values, scope, closures, decorators |
| 020 | PSE_020 | Builtins | range, enumerate, zip, map, filter, sorted |
| 030 | PSE_030 | Iterators / Generators | Iterable protocol, generator functions, yield |
| 040 | PSE_040 | Input / Output | print, input, file I/O, pathlib, serialization |
| 050 | PSE_050 | Modules | Imports, packages, virtual environments, pip |
| 060 | PSE_060 | Error Handling | try/except, custom exceptions, context managers |
| 070 | PSE_070 | Classes | Attributes, methods, properties, dataclasses |
| 080 | PSE_080 | OOP | 12 core OOP concepts |
| 090 | PSE_090 | Data Structures | Stack, queue, linked list, heap, tree, graph |
| 100 | PSE_100 | Type Hints | Basic typing, generics, protocols |
| 110 | PSE_110 | Concurrency | Threads, multiprocessing, async/await |
| 120 | PSE_120 | SOLID | 5 SOLID principles with examples |
| 130 | PSE_130 | Design Patterns | 23 GoF + 1 behavioral patterns |
| 135 | PSE_135 | Architectural Patterns | 5 enterprise architectural patterns |
| 140 | PSE_140 | Testing | unittest, pytest, mocking, fixtures |
| 150 | PSE_150 | Standard Library | collections, itertools, functools, datetime, json |
| 160 | PSE_160 | System Design | 17 distributed systems topics |
| 170 | PSE_170 | Algorithms | Big-O complexity, algorithm analysis |
| 180 | PSE_180 | CLI Frameworks | argparse, click, typer |
| 190 | PSE_190 | Serialization | pydantic, orjson, yaml, toml, msgpack |
| 200 | PSE_200 | Logging Advanced | structlog, loguru |
| 210 | PSE_210 | HTTP Client | httpx, requests |
| 220 | PSE_220 | Database | SQLAlchemy ORM, sqlite3 |
| 230 | PSE_230 | Web Frameworks | FastAPI, Flask |
| 240 | PSE_240 | Terminal UI | rich, textual |
| 250 | PSE_250 | GUI | tkinter (standard library) |
| 260 | PSE_260 | Packaging | pyproject.toml, uv |
| 270 | PSE_270 | Capstone | Full API server project |

## Topics Covered

### PSE_000 — Python Basics (9 files)

| # | File | Topics |
|---|------|--------|
| 01 | `PB_01_variables.py` | Variables, dynamic typing, unpacking |
| 02 | `PB_02_data_types.py` | int, float, str, bool, None |
| 03 | `PB_06_strings.py` | String operations, formatting |
| 04 | `PB_07_conditionals.py` | if / elif / else, ternary |
| 05 | `PB_08_loops.py` | for, while, enumerate, zip |
| 06 | `PB_09_lists.py` | Lists, slicing, comprehensions |
| 07 | `PB_10_tuples.py` | Tuples, named tuples |
| 08 | `PB_11_dictionaries.py` | Dicts, comprehensions |
| 09 | `PB_12_sets.py` | Sets, frozenset, set operations |

### PSE_010 — Functions (9 files)

| # | File | Topic |
|---|------|-------|
| 01 | `FN_01_basic_functions.py` | def, params, return, docstrings |
| 02 | `FN_02_parameters.py` | Positional, keyword, default, \*args, \*\*kwargs |
| 03 | `FN_03_return_values.py` | Return types, multiple returns, tuples |
| 04 | `FN_04_scope.py` | LEGB rule, global, nonlocal |
| 05 | `FN_05_args_kwargs.py` | \*args, \*\*kwargs, combined signatures |
| 06 | `FN_06_lambda.py` | Lambdas, map, filter, sorted |
| 07 | `FN_07_first_class_functions.py` | Passing and returning functions |
| 08 | `FN_08_closures.py` | nonlocal, factory functions |
| 09 | `FN_09_decorators.py` | @syntax, stacking, practical examples |

### PSE_020 — Builtins (10 files)

| # | File | Topic |
|---|------|-------|
| 01 | `BI_01_range.py` | range, sequences, loops |
| 02 | `BI_02_enumerate.py` | Index + value iteration |
| 03 | `BI_03_zip.py` | Combining iterables |
| 04 | `BI_04_map.py` | Applying functions to iterables |
| 05 | `BI_05_filter.py` | Filtering elements |
| 06 | `BI_06_sorted.py` | Sorting with key functions |
| 07 | `BI_07_reversed.py` | Reversing sequences |
| 08 | `BI_08_any_all.py` | Boolean aggregation |
| 09 | `BI_09_sum_min_max.py` | Numeric builtins |
| 10 | `BI_10_iter_next.py` | Iterator protocol |

### PSE_030 — Iterators / Generators (5 files)

| # | File | Topic |
|---|------|-------|
| 01 | `IT_01_iterable.py` | \_\_iter\_\_, \_\_next\_\_, for loop protocol |
| 02 | `IT_02_iterator.py` | Iterator protocol, custom iterators |
| 03 | `IT_03_generator.py` | Generator functions, lazy evaluation |
| 04 | `IT_04_yield.py` | yield, yield from, send() |
| 05 | `IT_05_generator_expression.py` | (expr for x in ...) syntax |

### PSE_040 — Input / Output (4 files)

| # | File | Topic |
|---|------|-------|
| 01 | `IO_01_print_input.py` | print(), input(), formatting |
| 02 | `IO_02_file_io.py` | open(), read/write, context managers |
| 03 | `IO_03_pathlib.py` | Path objects, glob, file operations |
| 04 | `IO_04_serialization.py` | json, pickle, csv |

### PSE_050 — Modules (4 files)

| # | File | Topic |
|---|------|-------|
| 01 | `MD_01_import.py` | import, from, as, \_\_name\_\_ |
| 02 | `MD_02_packages.py` | \_\_init\_\_, subpackages, relative imports |
| 03 | `MD_03_virtual_environment.py` | venv, pip, pyproject.toml |
| 04 | `MD_04_dependency_management.py` | Requirements files, lock files |

### PSE_060 — Error Handling (3 files)

| # | File | Topic |
|---|------|-------|
| 01 | `EH_01_exceptions.py` | try/except/finally, exception hierarchy |
| 02 | `EH_02_custom_exceptions.py` | Raising, custom error classes |
| 03 | `EH_03_context_managers.py` | with statement, \_\_enter\_\_/\_\_exit\_\_ |

### PSE_070 — Classes (10 files)

| # | File | Topic |
|---|------|-------|
| 01 | `CL_01_class_basics.py` | class, \_\_init\_\_, self |
| 02 | `CL_02_instance_attributes.py` | Instance variables, initialization |
| 03 | `CL_03_class_attributes.py` | Class-level state, shared data |
| 04 | `CL_04_instance_methods.py` | def methods, self parameter |
| 05 | `CL_05_class_methods.py` | @classmethod, factory methods |
| 06 | `CL_06_static_methods.py` | @staticmethod, utility functions |
| 07 | `CL_07_properties.py` | @property, getters, setters |
| 08 | `CL_08_private_attributes.py` | Name mangling, double underscore |
| 09 | `CL_09_magic_methods.py` | \_\_str\_\_, \_\_repr\_\_, \_\_len\_\_, operators |
| 10 | `CL_10_dataclasses.py` | @dataclass, field, frozen |

### PSE_080 — OOP (12 files)

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
| 09 | Abstract Classes | `OOP_09_abstract_classes.py` |
| 10 | Duck Typing | `OOP_10_duck_typing.py` |
| 11 | Protocols | `OOP_11_protocols.py` |
| 12 | Mixins | `OOP_12_mixins.py` |

### PSE_090 — Data Structures (6 files)

| # | File | Topic |
|---|------|-------|
| 01 | `DS_01_stack.py` | LIFO, push/pop, balanced parentheses |
| 02 | `DS_02_queue.py` | FIFO, deque, BFS |
| 03 | `DS_03_linked_list.py` | Singly/doubly linked nodes |
| 04 | `DS_04_heap.py` | Min/max heap, heapq |
| 05 | `DS_05_tree.py` | TreeNode, BST, traversal |
| 06 | `DS_06_graph.py` | Adjacency list, BFS, DFS |

### PSE_100 — Type Hints (4 files)

| # | File | Topic |
|---|------|-------|
| 01 | `TH_01_basic_typing.py` | int, str, List, Dict, Optional |
| 02 | `TH_02_generics.py` | TypeVar, Generic, Callable |
| 03 | `TH_03_protocols.py` | Structural subtyping |
| 04 | `TH_04_type_alias.py` | Type aliases, NewType |

### PSE_110 — Concurrency (5 files)

| # | File | Topic |
|---|------|-------|
| 01 | `CC_01_cpu_vs_io_bound.py` | When to use threads vs processes |
| 02 | `CC_02_threads.py` | threading, Lock, GIL, thread safety |
| 03 | `CC_03_multiprocessing.py` | Process Pool, parallel CPU work |
| 04 | `CC_04_asyncio.py` | Event loop, coroutines, gather |
| 05 | `CC_05_async_await.py` | async def, await, async queues |

### PSE_120 — SOLID Principles (5 files)

| # | Principle | File |
|---|-----------|------|
| 01 | Single Responsibility | `SOLID_01_single_responsibility.py` |
| 02 | Open/Closed | `SOLID_02_open_closed.py` |
| 03 | Liskov Substitution | `SOLID_03_liskov_substitution.py` |
| 04 | Interface Segregation | `SOLID_04_interface_segregation.py` |
| 05 | Dependency Inversion | `SOLID_05_dependency_inversion.py` |

### PSE_130 — Design Patterns (24 files)

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
| | 12 | Null Object | `Behavioral/DP_B_12_null_object_pattern.py` |

All 23 classic Gang of Four patterns + 1 additional behavioral pattern (Null Object).

### PSE_135 — Architectural Patterns (5 files)

| # | Pattern | File |
|---|---------|------|
| 01 | Repository | `AP_01_repository.py` |
| 02 | Dependency Injection | `AP_02_dependency_injection.py` |
| 03 | Unit of Work | `AP_03_unit_of_work.py` |
| 04 | Event Sourcing | `AP_04_event_sourcing.py` |
| 05 | CQRS | `AP_05_cqrs.py` |

### PSE_140 — Testing (4 files)

| # | File | Topic |
|---|------|-------|
| 01 | `TS_01_unittest.py` | TestCase, setUp, assertions |
| 02 | `TS_02_pytest.py` | pytest syntax, parametrize |
| 03 | `TS_03_mocking.py` | unittest.mock, patch |
| 04 | `TS_04_fixtures.py` | pytest fixtures, scope, teardown |

### PSE_150 — Standard Library (8 files)

| # | File | Topic |
|---|------|-------|
| 01 | `SL_01_collections.py` | defaultdict, Counter, deque, namedtuple |
| 02 | `SL_02_itertools.py` | chain, product, combinations, permutations |
| 03 | `SL_03_functools.py` | reduce, partial, lru_cache, wraps |
| 04 | `SL_04_datetime.py` | date, time, timedelta, strftime |
| 05 | `SL_05_pathlib.py` | Path, glob, suffix, parent |
| 06 | `SL_06_json.py` | dumps, loads, custom encoding |
| 07 | `SL_07_csv.py` | reader, writer, DictReader |
| 08 | `SL_08_logging.py` | levels, handlers, basicConfig |

### PSE_160 — System Design (17 files)

| # | File | Topic |
|---|------|-------|
| 01 | `SD_01_client_server.py` | Client-server architecture |
| 02 | `SD_02_http_rest.py` | HTTP methods, REST API design |
| 03 | `SD_03_dns.py` | DNS resolution, load balancing |
| 04 | `SD_04_load_balancing.py` | Round-robin, least connections |
| 05 | `SD_05_caching.py` | Cache-aside pattern, cache vs DB |
| 06 | `SD_06_rate_limiting.py` | Token bucket, sliding window |
| 07 | `SD_07_message_queue.py` | Pub/sub, task queues |
| 08 | `SD_08_database_replication.py` | Primary-replica, read replicas |
| 09 | `SD_09_database_indexing.py` | B-tree, composite indexes |
| 10 | `SD_10_sharding.py` | Horizontal partitioning, shard keys |
| 11 | `SD_11_consistent_hashing.py` | Hash rings, virtual nodes |
| 12 | `SD_12_proxy.py` | Forward proxy, reverse proxy |
| 13 | `SD_13_microservices.py` | Service decomposition, API gateway |
| 14 | `SD_14_pub_sub.py` | Topics, subscribers, fan-out |
| 15 | `SD_15_url_shortener.py` | Encoding, redirection, analytics |
| 16 | `SD_16_cdn.py` | Edge caching, geographic routing |
| 17 | `SD_17_cap_theorem.py` | Consistency, availability, partition tolerance |

### PSE_170 — Algorithms (1 file)

| # | File | Topic |
|---|------|-------|
| 01 | `AL_01_big_o.py` | O(1), O(log n), O(n), O(n²), space complexity |

### PSE_180 — CLI Frameworks (3 files)

| # | File | Topic |
|---|------|-------|
| 01 | `CLI_01_argparse.py` | argparse, subcommands, argument groups |
| 02 | `CLI_02_click.py` | click decorators, options, groups |
| 03 | `CLI_03_typer.py` | typer with type hints, enums |

### PSE_190 — Serialization (2 files)

| # | File | Topic |
|---|------|-------|
| 01 | `SER_01_pydantic.py` | Pydantic models, validation, serialization |
| 02 | `SER_02_json_formats.py` | json, orjson, yaml, toml, msgpack |

### PSE_200 — Logging Advanced (2 files)

| # | File | Topic |
|---|------|-------|
| 01 | `LOG_01_structlog.py` | Structured logging, JSON output |
| 02 | `LOG_02_loguru.py` | Zero-config logging, rotation, async |

### PSE_210 — HTTP Client (2 files)

| # | File | Topic |
|---|------|-------|
| 01 | `HTTP_01_httpx.py` | httpx sync/async, sessions, streaming |
| 02 | `HTTP_02_requests.py` | requests (legacy reference) |

### PSE_220 — Database (2 files)

| # | File | Topic |
|---|------|-------|
| 01 | `DB_01_sqlalchemy.py` | SQLAlchemy ORM, models, relationships |
| 02 | `DB_02_sqlite3.py` | sqlite3 stdlib, CRUD, transactions |

### PSE_230 — Web Frameworks (2 files)

| # | File | Topic |
|---|------|-------|
| 01 | `WEB_01_fastapi.py` | FastAPI routes, Pydantic, dependencies |
| 02 | `WEB_02_flask.py` | Flask routes, request/response |

### PSE_240 — Terminal UI (2 files)

| # | File | Topic |
|---|------|-------|
| 01 | `TUI_01_rich.py` | Tables, progress bars, syntax highlighting |
| 02 | `TUI_02_textual.py` | TUI apps, widgets, CSS styling |

### PSE_250 — GUI (1 file)

| # | File | Topic |
|---|------|-------|
| 01 | `GUI_01_tkinter.py` | Widgets, layouts, events |

### PSE_260 — Packaging (2 files)

| # | File | Topic |
|---|------|-------|
| 01 | `PKG_01_pyproject.toml.py` | pyproject.toml structure, tool config |
| 02 | `PKG_02_uv.py` | uv package manager commands |

### PSE_270 — Capstone (1 file)

| # | File | Topic |
|---|------|-------|
| 01 | `CAP_01_api_server.py` | Full API with FastAPI + SQLAlchemy + tests |

## How To Use

Run any example directly with Python:

```bash
python PSE_000_Python_Basics/PB_01_variables.py
python PSE_010_Functions/FN_09_decorators.py
python PSE_080_OOP/OOP_04_abstraction.py
python PSE_120_SOLID/SOLID_01_single_responsibility.py
python PSE_130_Design_Patterns/Creational/DP_C_01_singleton_pattern.py
python PSE_135_Architectural_Patterns/AP_04_event_sourcing.py
python PSE_135_Architectural_Patterns/AP_05_cqrs.py
python PSE_160_System_Design/SD_05_caching.py
python PSE_160_System_Design/SD_16_cdn.py
python PSE_110_Concurrency/CC_04_asyncio.py
python PSE_170_Algorithms/AL_01_big_o.py
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
- Number gaps (180+) are reserved for future topics.
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
