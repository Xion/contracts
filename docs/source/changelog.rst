Changelog
=========

.. _changelog: 


1.2.0 -- 2011-09-01
--------------------

* Mainly speed improvements.

1.1.0 -- 2011-06-30
--------------------

* Now Numpy array are treated as sequences: ``seq[2](number)`` matches both ``[1,2]``
  as well as ``np.array([1,2])``.

1.0.0 -- 2011-06-30
--------------------

No new features since 0.9.4, mainly performance improvements and some bug fixes.

Main changes:

* Fixed bug that did not allow to define new contracts with name such as `list_`` if ``list``
  is already defined.
  
* Performance much improved when contracts is disabled; now the overhead is only an extra function call.



0.9.4 -- 2011-03-19
--------------------

Bug fixes:

* Fixed bugs with ``new_contract`` with new contract names composed
  by only two letters (it confused the parsing rules).

Performance improvements:

* Avoid deep copy of objects in some cases (thanks to William Furr),

New experimental features:

* Contracts for class methods (suggestion by William Furr). 
  Documentation still to write; here's an example: ::
  
    from contracts import new_contract, contract

    class Game(object):
        def __init__(self, legal_moves):
            self.legal_moves = legal_moves

        # You can now create a contract from object methods
        # that can use the object attributes to validate the value.
        @new_contract
        def legal_move(self, move):
            if not move in self.legal_moves:
                raise ValueError('Move not valid')

        @contract(move='legal_move')
        def take_turn(self, move):
            pass
        
    game = Game(legal_moves=[1,2,3])
    game.take_turn(1) # ok
    game.take_turn(5) # raises exception



0.9.3 -- 2011-01-28
--------------------

New features:

* Interface change: the decorator is now called ``contract`` instead of ``contracts``,
  because ``from contracts import contracts`` looked quite clumsy
  (the old form is still available).
  
* The ``@contract`` decorator now changes the function's docstring to show the contracts for the parameters. See `an example application`__.

* Implemented the generic contracts ``seq`` and ``map`` that
  generalize ``list`` and ``dict`` when any Sequence or Mapping will do. 
  
* Added element-by-element tests in ``array``. Now in an expression of the
  kind ``array(>=0|<-1)`` the expression will be evaluate element by element.

* Implemented ``pi`` as a special constant that can be used in the contracts.

* Now it is possible to give more context to calls to ``check`` and ``fail`` 
  through the use of keywords variable. For example:: 
  
      check('array[*xM]', a,  M=2)

* Added a function ``disable_all()`` that disables all testing done by PyContracts.
  This can be used to make sure that PyContracts is not slowing things down.

Various fixes:

* Fixed missing files in source distribution (thanks to Bernhard Biskup).

* Much better error messages.

* The functions signatures are now conserved  (using the ``decorator`` module). 
      
* ``Contract`` objects and Exceptions can be safely pickled. 

* In many cases, the exceptions are caught and re-raised to give a clearer stack trace.


.. __: http://andreacensi.github.com/geometry/api.html


0.9.2 -- Released 2010-12-27
----------------------------

(changelog not available)
