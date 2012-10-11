# ================================================================================
# Project:   Kivy.Statechart - A Statechart Framework for Kivy
# Copyright: (c) 2010, 2011 Michael Cohen, and contributors.
# Python Port: Jeff Pittman, ported from SproutCore, SC.Statechart
# ================================================================================

import inspect

"""
  Singleton
"""
class AsyncMixin:

    """
      Call in either a state's enter_state or exit_state method when you
      want a state to perform an asynchronous action, such as an animation.

      Examples:

        State.extend({

          enter_state: function() {
            return Async.perform('foo');
          },

          exit_state: function() {
            return Async.perform('bar', 100);
          }

          foo: function() { ... },

          bar: function(arg) { ... }

        });

      @param func {String|Function} the function to be invoked on a state
      @param arg1 Optional. An argument to pass to the given function
      @param arg2 Optional. An argument to pass to the given function
      @return {Async} a new instance of a Async
    """
    def perform(self, func, arg1=None, arg2=None):
        return Async(func, arg1=arg1, arg2=arg2)

"""
  @class

  Represents a call that is intended to be asynchronous. This is
  used during a state transition process when either entering or
  exiting a state.

  @extends Object
  @author Michael Cohen
"""
class Async(AsyncMixin):
    def __init__(self, func, arg1=None, arg2=None):
        self.func = func
        self.arg1 = arg1
        self.arg2 = arg2

    """ @private
      Called by the statechart
    """
    def try_to_perform(self, state):
        if isinstance(self.func, basestring):
            if hasattr(state, self.func):
              getattr(state, self.func)(self.arg1, self.arg2)
        elif inspect.isfunction(self.func) or inspect.ismethod(self.func): # [PORT] Either one, same call sig?
            self.func(state, self.arg1, self.arg2)
