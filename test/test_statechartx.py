# -*- code: utf-8 -*-
"""Unit test cases for module statechartx."""

import pytest
from statechart import Statechart

from statechartx import TerminalState, Workflow, WorkflowFactory, WorkflowMetadata


# pylint: disable=redefined-outer-name, no-self-use, too-few-public-methods


class DummyState(TerminalState):
    """A dummy implementation of TerminalState."""

    def init(self):
        self.param_a = self.metadata.param_a


class DummyWorkflow(Workflow):
    """A dummy implementation of Workflow."""

    def init(self, factory):
        self.state = factory.create_state("dummy-state", self, DummyState)


@pytest.fixture
def metadata():
    """Returns fixture of a WorkflowMetadata instance."""
    return WorkflowMetadata(param_a=1, param_b="foo", param_c=[1], param_d={1: "foo"})


@pytest.fixture
def factory(metadata):
    """Returns fixture of a WorkflowFactory instance."""
    return WorkflowFactory(metadata)


@pytest.fixture
def context():
    """Returns fixture of a Statechart instance."""
    return Statechart("context")


class TestWorkflowMetadata:
    """Unit test cases for class WorkflowMetadata."""

    def test_init(self, metadata):
        """Tests initialisation."""
        assert metadata.param_a == 1
        assert metadata.param_b == "foo"
        assert metadata.param_c == [1]
        assert metadata.param_d == {1: "foo"}


class TestTerminalState:
    """Unit test cases for class TerminalState."""

    def test_init(self, factory, context):
        """Tests initialisation."""
        state = factory.create_state("test-state", context, DummyState)

        assert state.name == "test-state"
        assert state.param_a == 1


class TestWorkflow:
    """Unit test cases for class Workflow."""

    def test_init(self, factory, context):
        """Tests initialisation."""
        workflow = factory.create_workflow("test-workflow", context, DummyWorkflow)

        assert workflow.name == "test-workflow"
        assert workflow.state.name == "dummy-state"
        assert workflow.state.param_a == 1


class TestWorkflowFactory:
    """Unit test cases for class WorkflowFactory."""

    def test_create_state(self, factory, context):
        """Tests creation of a state."""
        state = factory.create_state("test-state", context, DummyState)

        assert state.name == "test-state"
        assert state.param_a == 1

    def test_create_workflow(self, factory, context):
        """Tests creation of a workflow."""
        workflow = factory.create_workflow("test-workflow", context, DummyWorkflow)

        assert workflow.name == "test-workflow"
        assert workflow.state.name == "dummy-state"
        assert workflow.state.param_a == 1
