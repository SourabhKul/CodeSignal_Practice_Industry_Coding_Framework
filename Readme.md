# Mock CodeSignal Pre-screen: INDUSTRY CODING FRAMEWORK

This serves as a mock example of an industry coding framework assessment, similar to those found in pre-screens on CodeSignal. It's important to highlight the rarity of comprehensive guides or examples on navigating these types of assessments on the internet, making this document an invaluable resource for those seeking to prepare for such challenges 🚀.

For more insights and resources, follow the creator on Twitter [@PaulLockettkpb](https://twitter.com/PaulLockettkpb).

This guide is part of his journey in exploring and sharing knowledge within the coding community.

The tasks outlined in this document are crafted to emulate the complexity and breadth of coding assessments typically encountered during technical interviews or coding competitions 🧩. Each level introduces incrementally more complex problems, requiring a solid understanding of data structures, algorithms, and software engineering principles 📚.

For the Anthropic-focused, evidence-labeled practice sequence, start with [`anthropic_prep/README.md`](anthropic_prep/README.md). It contains the high-signal reported scenario families, progressive candidate workspaces, and separate reference answers for review after each attempt.

## Pre-requisites

Before diving into the tasks and running the tests outlined in this guide, it's crucial to ensure that your development environment is properly set up. Here are the prerequisites necessary to run the test and simulation effectively:

1. **Python Installation**: Use Python 3.10 or newer for this local practice pack. CodeSignal publishes support for Python 3 but does not promise a fixed patch version, so the rules in your actual assessment invitation are authoritative.

2. **Familiarity with Terminal or Command Prompt**: Basic knowledge of using the terminal (Mac/Linux) or command prompt (Windows) will be beneficial. You will need it to run each drill's `test_solution.py` file.

3. **Install Required Python Packages**: Before starting with the tasks, it's essential to install the Python packages listed in the `requirements.txt` file. To install them, run the following command in your terminal or command prompt:

   ```bash
   pip install -r requirements.txt
   ```

   The file intentionally installs no third-party packages. Industry Coding Assessment drills should be solvable with the standard library.

By ensuring these prerequisites are met, you will be well-prepared to engage with the tasks, run tests, and make the most out of this mock CodeSignal pre-screen assessment. Remember, a well-set-up development environment is key to a smooth and efficient coding experience.

## How to Use This Mock Assessment

1. **Timing**: Set a strict time limit of 90 minutes for yourself to complete the tasks ⏳. This practice is designed to simulate the time constraints often present in real assessments, fostering the development of effective time management skills.
2. **Sequential Progression**: Start with Level 1 and do not advance to the subsequent level until you have fully completed the preceding one 🛤️. This methodical approach ensures a gradual and thorough understanding of the challenges presented.

3. **Testing and Development Environment**: Focus your coding efforts within a drill's `solution.py` file 🖥️. Read `level1.md` through `level4.md` one at a time and add each newly unlocked interface.

4. **Running Tests**: Use the drill's `test_solution.py` file to verify each level incrementally 🧪. For example:

   - For Level 1: `python3 -m unittest test_solution.TestChineseRestaurant.test_level_1_seating`
   - For Level 2: `python3 -m unittest test_solution.TestChineseRestaurant.test_level_2_bulk_and_ranking`
   - For subsequent levels, use the matching test name listed in that drill's `prompt.md`.

5. **Refactoring**: As you progress through the levels, revisit and refactor your earlier solutions as needed to accommodate the additional functionality required by later tasks 🔧. This iterative process is key to developing scalable and maintainable software.

To ensure the fastest possible progression through the levels, consider the following strategies:

1. **Familiarize Yourself with the Framework**: Before starting the timer, spend some time understanding the coding framework and the structure of the tasks (see the pdf in this repo) 📖. This upfront investment will pay dividends by reducing the time needed to interpret tasks during the timed session.

2. **Plan Before You Code**: For each task, spend a few minutes planning your approach before you start coding 📝. This can include writing pseudocode, drawing diagrams, or outlining the steps you need to take. A clear plan will help you code more efficiently and reduce the time spent on debugging.

3. **Practice Speed Typing**: The physical act of typing can be a bottleneck 🚀. Improving your typing speed through practice can have a surprisingly significant impact on your overall speed.

4. **Master the Art of Skimming**: Learn to quickly skim the task descriptions to identify the key requirements and constraints 🔍. This skill will allow you to start formulating your solution even as you finish reading the task.

5. **Use the Standard Library Well**: Be fluent with dictionaries, sets, sorting keys, `collections`, and `bisect`, but do not depend on third-party packages.

6. **Parallelize Testing and Coding**: If possible, set up your environment so you can run tests on the code you've already written while continuing to work on other parts of the task 🔄. This can help identify issues early and reduce overall development time.

7. **Focus on Passing Tests Over Perfection**: Aim to get a working solution as quickly as possible, even if it's not the most elegant 🎯. You can always refactor later if you have time remaining.

By incorporating these strategies, you can significantly increase your speed and efficiency, allowing you to progress through the levels at an accelerated pace ⚡.

The following table, sourced from [How hackable are automated coding assessments?](https://yanirseroussi.com/2023/05/26/how-hackable-are-automated-coding-assessments/), offers a detailed breakdown of the expected time allocation for questions within Industry Coding Assessments. It is formatted for clear understanding and reference:

| Level | Expected Time (minutes) |
| ----- | ----------------------- |
| 1     | 10-15                   |
| 2     | 20-30                   |
| 3     | 30-60                   |
| 4     | 30-60                   |

When aggregating the time ranges across all levels, the cumulative estimate to complete the assessment ranges from 90 to 165 minutes. However, the stipulated completion time for candidates is set at 90 minutes. This discrepancy is intentional and serves a specific purpose as outlined below:

> The assessment's maximum allowed completion time is capped at 90 minutes. This constraint is not an expectation for candidates to solve all tasks within this limit. The rationale behind shorter assessments, despite their potential for a more accurate measurement of candidate skills, is rooted in the observation that candidate willingness to engage with the assessment drops significantly for tests exceeding 2 hours in duration. A critical aspect of evaluating candidates' capabilities lies in observing the extent of their progression within the allocated timeframe, rather than the completion of all tasks.

Adhering to these guidelines and completing the tasks within the designated time frame will equip you with practical experience in tackling coding assessments.

Best of luck, and remember to frequently test your solutions to track your progress and obtain feedback on your approach 🍀.

## How to Contribute

Contributing to this guide is a fantastic way to help others prepare for industry coding assessments. If you're interested in adding more questions and challenges, we welcome your contributions! Here's how you can contribute:

1. **Understand the Framework**: Before creating new questions, please familiarize yourself with the existing coding framework and the structure of the tasks. Refer to the PDF in this repository for detailed guidelines on how questions should be structured and what they aim to assess.

2. **Create New Questions**: Design your questions to mimic real-world coding assessments. Ensure they are clear, concise, and cover a range of difficulties. Each question should challenge a specific skill or set of skills relevant to coding assessments, such as algorithmic thinking, data structures, or problem-solving under time constraints.

3. **Follow the Existing Structure**: New questions should match the progressive structure under `anthropic_prep/oa_progressive`: four level files, a candidate workspace, grouped tests, and a separate reference solution.

4. **Adhere to the PDF Guidelines**: The PDF in the repository outlines the rules for how questions should work. Please ensure your questions comply with these rules to maintain the quality and relevance of the assessments.

5. **Submit Your Questions**: Place each new question in its own subdirectory under `anthropic_prep/oa_progressive`.

6. **Open a Pull Request**: Submit your contributions via a pull request. In your pull request, provide a brief explanation of your questions and how they align with the objectives of the coding framework. Our team will review your submission and provide feedback if necessary.

7. **Stay Engaged**: After submitting your questions, stay engaged with the community. Respond to feedback on your pull request and be open to making adjustments to your questions as recommended by reviewers.

By contributing to this guide, you're not only helping others prepare for their coding assessments but also honing your own skills in creating meaningful, challenging coding problems. We look forward to seeing your contributions and expanding our collection of practice assessments!

## Usage with uv

uv is a modern Python package management solution which enables this application to be run in an isolated virtual environment.

[Install uv as described here](https://docs.astral.sh/uv/getting-started/installation/), then:

```bash
uv venv
source .venv/bin/activate
# or, `source .venv/Scripts/activate` on Windows
uv pip install -r requirements.txt
```

Now you can update the relevant `solution.py` and run that drill's tests.

For example, to run the Chinese Restaurant Process drill:

```bash
cd anthropic_prep/oa_progressive/chinese_restaurant_process
python3 test_solution.py
```
