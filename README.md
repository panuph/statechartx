# statechartx

This Python package, statechartx, is a trivial extension to Leigh McKenzie's statechart, Python UML
statechart framework.

This extension has introduced the concept of terminal state and workflow (or non-terminal state). A
terminal state (class TerminalState) is equivalent to statechart's class State, which itself does
not contain any other states. A workflow (class Workflow) is equivalent to statechart's class
CompositeState, which itself contains other terminal states and workflows.

The goal of this extension is to simplify and ease the way a workflow is created and defined. This
extension is by no means a layer of software on top of statechart, as the user still has to use
statechart to achieve their goal. See the example code in example.py for example usage.


## Dependencies

See file requirements.txt.


## Installation

pip install statechartx
