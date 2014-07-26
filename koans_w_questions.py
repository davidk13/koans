    #couldn't solve this koan exercise
    #I thought the answer in line 22 was NameError but that didn't seem to work
    #I thought the answer in line 27 was 
    #'name "some_method_none_does_not_know_about" is not defined'
    #but that didn't seem to work 
     def test_what_exception_do_you_get_when_calling_nonexistent_methods(self):
        """
        What is the Exception that is thrown when you call a method that does
        not exist?

        Hint: launch python command console and try the code in the
        block below.

        Don't worry about what 'try' and 'except' do, we'll talk about
        this later
        """
        try:
            None.some_method_none_does_not_know_about()
        except Exception as ex:
            # What exception has been caught?
            #
            # Need a recap on how to evaluate __class__ attributes?
            #   https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute

            self.assertEqual(__, ex.__class__)

            # What message was attached to the exception?
            # (HINT: replace __ with part of the error message.)
            self.assertMatch(__, ex.args[0])
    
