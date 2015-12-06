# Look for #IMPLEMENT tags in this file. These tags indicate what has
# to be implemented to complete the warehouse domain.

from collections import deque

'''This file will contain different constraint propagators to be used within
   bt_search.

   propagator == a function with the following template
      propagator(csp, newly_instantiated_variable=None)
           ==> returns (True/False, [(Variable, Value), (Variable, Value) ...]

      csp is a CSP object---the propagator can use this to get access
      to the variables and constraints of the problem. The assigned variables
      can be accessed via methods, the values assigned can also be accessed.

      newly_instaniated_variable is an optional argument.
      if newly_instantiated_variable is not None:
          then newly_instantiated_variable is the most
           recently assigned variable of the search.
      else:
          progator is called before any assignments are made
          in which case it must decide what processing to do
           prior to any variables being assigned. SEE BELOW

       The propagator returns True/False and a list of (Variable, Value) pairs.
       Return is False if a deadend has been detected by the propagator.
       in this case bt_search will backtrack
       return is true if we can continue.

      The list of variable values pairs are all of the values
      the propagator pruned (using the variable's prune_value method).
      bt_search NEEDS to know this in order to correctly restore these
      values when it undoes a variable assignment.

      NOTE propagator SHOULD NOT prune a value that has already been
      pruned! Nor should it prune a value twice

      PROPAGATOR called with newly_instantiated_variable = None
      PROCESSING REQUIRED:
        for plain backtracking (where we only check fully instantiated constraints)
        we do nothing...return true, []

        for forward checking (where we only check constraints with one remaining variable)
        we look for unary constraints of the csp (constraints whose scope contains
        only one variable) and we forward_check these constraints.

        for gac we establish initial GAC by initializing the GAC queue
        with all constaints of the csp


      PROPAGATOR called with newly_instantiated_variable = a variable V
      PROCESSING REQUIRED:
         for plain backtracking we check all constraints with V (see csp method
         get_cons_with_var) that are fully assigned.

         for forward checking we forward check all constraints with V
         that have one unassigned variable left

         for gac we initialize the GAC queue with all constraints containing V.

   '''


def prop_BT(csp, newVar=None):
    '''Do plain backtracking propagation. That is, do no
    propagation at all. Just check fully instantiated constraints'''

    if not newVar:
        return True, []
    for c in csp.get_cons_with_var(newVar):
        if c.get_n_unasgn() == 0:
            vals = []
            vars = c.get_scope()
            for var in vars:
                vals.append(var.get_assigned_value())
            if not c.check(vals):
                return False, []
    return True, []


pruned_values = []


def prop_FC(csp, newVar=None):
    '''Do forward checking. That is check constraints with
       only one uninstantiated variable. Remember to keep
       track of all pruned variable,value pairs and return '''

    global pruned_values
    pruned_values = []
    if not newVar:
        all_cons = csp.get_all_cons()
        for constraint in all_cons:
            # forward check only constraints with one unassigned variable
            if constraint.get_n_unasgn() == 1:
                unassigned_var = constraint.get_unasgn_vars()
                V = unassigned_var[0]
                if FCCheck(constraint, V):
                    return (False, pruned_values)

        return (True, pruned_values)

    else:
        all_cons = csp.get_cons_with_var(newVar)
        for constraint in all_cons:
            unassigned_vars = constraint.get_unasgn_vars()
            if len(unassigned_vars) == 1:
                var = unassigned_vars[0]
                if FCCheck(constraint, var):
                    return (False, pruned_values)

        return (True, pruned_values)


def FCCheck(C, x):
    ''' C is a constraint with all of its variables assigned,
        except for variable x.
         '''

    scope = C.get_scope()
    variables = [val.get_assigned_value() for val in scope]

    index = 0
    for val in variables:
        if val is None:
            break
        index += 1

    for d in x.cur_domain():
        variables[index] = d
        if not C.check(variables) and (x, d) not in pruned_values:
            x.prune_value(d)
            pruned_values.append((x, d))

    # A return of True indicates DWO.
    if x.cur_domain_size() == 0:
        return True
    return False


def prop_GAC(csp, newVar=None):
    '''Do GAC propagation. If newVar is None we do initial GAC enforce
       processing all constraints. Otherwise we do GAC enforce with
       constraints containing newVar on GAC Queue'''

    GACQueue = deque()
    pruned = []

    if not newVar:
        GACQueue.extend(csp.get_all_cons())
    else:
        GACQueue.extend(csp.get_cons_with_var(newVar))

    while len(GACQueue) != 0:
        C = GACQueue.popleft()
        for V in C.get_unasgn_vars():

            for d in V.cur_domain():
                check = C.has_support(V, d)
                if not check:
                    V.prune_value(d)
                    pruned.append((V, d))
                    if V.cur_domain_size() == 0:
                        return (False, pruned)

                    new_constraints = [
                        x for x in csp.get_cons_with_var(V) if x not in GACQueue and x is not C]
                    GACQueue.extend(new_constraints)

    return (True, pruned)
