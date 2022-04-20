------------------------------ MODULE Calendar ------------------------------

EXTENDS Integers
VARIABLES user, action,authentify,typeEmployee,choicesMan,choicesEmp,accepts
INIT == ((user \in [0 .. 2])
        /\(authentify \in[0 .. 1])
        /\(typeEmployee \in[0..1])
        /\(choicesMan \in[0 .. 3])
        /\(choicesEmp \in[0 .. 2])
        /\(accepts \in[0 .. 1]))
NEXT ==( ((pc = "step1")
    
        \/((user = 0)
             
                ((action = "Registered")/\(user' \in [0 .. 2]))
                /\((authentify = 1)
                     
                        ((action' = "Authentification successfull")/\ ( authentify' \in[0 .. 1])/\(pc'="step2")))
                
               \/
                    
                        ((action' = "Authentification unsuccessfull")/\ ( authentify' \in[0 .. 1]))))
                
                
        \/((user = 1)
            THEN
                 \/((authentify = 1)
                    
                        ((action' = "Authentification successfull")/\ ( authentify' \in[0 .. 1])/\(pc'="step2")))
                 \/
                    
                        ((action' = "Authentification unsuccessfull")/\ ( authentify' \in[0 .. 1])))
         \/((user = 2)
            
                 \/((authentify = 1)
                     
                        ((action' = "Authentification successfull")/\ ( authentify' \in[0 .. 1])/\(pc'="step2")))
                 \/
                    
                        ((action' = "Authentification unsuccessfull")/\ ( authentify' \in[0 .. 1])))
((pc = "step2")
    
        \/((typeEmployee = 0)
             
                ((action' = "Display Manager window and options")/\(pc = "step3")))
        \/
            
                ((action' = "Display Manager window and options")/\(pc = "step4")))
                
((pc = "step3")
     
        \/(( choicesMan = 0)
            
                 /\((action' = "Display Manager calendar")/\(pc ="step3")/\(choicesMan' \in [0 .. 3])))
         \/(( choicesMan = 1)
            
               /\ ((action' = "Made a request to employees")/\(pc ="step3")/\(choicesMan' \in [0 .. 3])))
         \/(( choicesMan = 2)
            
                /\((action' = "Check employee request")/\(pc ="step3")/\(choicesMan' \in [0 .. 3])))
                \/(((accepts = 1)
                    
                       /\ ((accepts' \in [0 .. 1])/\(action' = "Employee request Accepted, rescheduling")/\(pc ="step3")))
                
                 
                      \/  ((accepts' \in [0 .. 1])/\(action' = "Employee request Denied")/\(pc ="step3")))
                
         \/(( choicesMan = 3)
            
                /\((action' = "Create schedule")/\(pc ="step3")/\(choicesMan' \in [0 .. 3])))
         \/FALSE)
((pc = "step4")
    
         \/(( choicesMan = 0)
            
                 /\((action' = "Display Manager calendar")/\(pc ="step3")/\(choicesMan' \in [0 .. 3])))
         \/(( choicesMan = 1)
            
                /\((action' = "Made a request to employees")/\(pc ="step3")/\(choicesMan' \in [0 .. 3])))
         \/(( choicesMan = 2)
            
                /\(((action' = "Check employee request")/\(pc ="step3")/\(choicesMan' \in [0 .. 3]))
                 /\((accepts = 1)
                    
                       /\ ((accepts' \in [0 .. 1])/\(action' = "Employee request Accepted, rescheduling")/\(pc ="step3")))
                   \/
                    
                        ((accepts' \in [0 .. 1])/\(action' = "Employee request Denied")/\(pc ="step3")))))
          \/FALSE)
           
)
        
    
=============================================================================
\* Modification History
\* Last modified Tue Apr 19 22:21:53 BOT 2022 by rosey
\* Created Tue Apr 19 18:31:49 BOT 2022 by rosey
