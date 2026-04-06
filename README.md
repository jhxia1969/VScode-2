<<<<<<< HEAD
<header>

<!--
  <<< Author notes: Course header >>>
  Read <https://skills.github.com/quickstart> for more information about how to build courses using this template.
  Include a 1280×640 image, course name in sentence case, and a concise description in emphasis.
  In your repository settings: enable template repository, add your 1280×640 social image, auto delete head branches.
  Next to "About", add description & tags; disable releases, packages, & environments.
  Add your open source license, GitHub uses the MIT license.
-->

# Code with GitHub Codespaces and Visual Studio Code

_Develop code using GitHub Codespaces and Visual Studio Code!_

</header>

```text
all_in_one_toolkit/
  src/
    main.py
    core/
      calculator.py
      data_cleaner.py
      file_automation.py
  tests/
    test_calculator.py
    test_data_cleaner.py
```

## 运行方式

在项目根目录执行：

```bash
python src/main.py calc --op add --a 10 --b 5
python src/main.py clean-csv --input input.csv --output output.csv
python src/main.py batch-rename --dir . --prefix image --start 1 --ext .png --dry-run
python src/main.py chart
```

## 运行测试

```bash
python -m unittest discover -s tests -v
```
