--------------------------- MODULE CalendarMark2 ---------------------------
EXTENDS Integers
VARIABLES choice, pc, persona


Init == /\  (choice = 0)
        /\  (pc = "Begin")
        /\  ( persona = 0)
        
TypeOk == /\ (choice'\in 0..5)
          /\  (persona' \in 0..2)
        
        
ViewCalendar == IF choice = 0 /\ ( persona = 0 \/ persona = 1)
                    THEN
                        pc'= "Viewing Calendar" 
                        /\ UNCHANGED<<choice,persona>>
                    ELSE
                        pc'= "log in failed try again or Need to register"
                        /\ UNCHANGED<<choice,persona>>
AcceptDeny ==  IF choice = 1 /\ ( persona = 0 \/ persona = 1)
                    THEN
                        pc'= "Accepted/Denied request - Sending notification"
                        /\ UNCHANGED<<choice,persona>>
                    ELSE
                        pc'= "log in failed try again or Need to register"
                        /\ UNCHANGED<<choice,persona>>
CreateSchedule == IF choice = 2 /\ persona = 0 
                     THEN
                        pc'= "Schedule changes made - Sending notification"
                        /\ UNCHANGED<<choice,persona>>
                     ELSE
                        pc'= " You do not have access right to this feature or Need to register"
                        /\ UNCHANGED<<choice,persona>>
Request == IF choice = 3 /\ ( persona = 0 \/ persona = 1)
                    THEN
                        pc'= "You have sucessfully made a request - Sending notification"
                        /\ UNCHANGED<<choice,persona>>
                    ELSE
                        pc'= "log in failed try again or Need to register"
                        /\ UNCHANGED<<choice,persona>>
Register == IF choice = 4 /\ persona = 3 
                    THEN
                        pc'= "You have registered successfully - Sending notification"
                        /\ UNCHANGED<<choice,persona>>
                    ELSE
                        pc'= "This user already exists - Try again"
                        /\ UNCHANGED<<choice,persona>>
RescheduleSchedule == IF choice = 2 /\ persona = 0 
                            THEN
                        pc'= "Schedule changes made - Sending notification"
                        /\ UNCHANGED<<choice,persona>>
                     ELSE
                        pc'= " You do not have access right to this feature or Need to register"
                        /\ UNCHANGED<<choice,persona>>
                        
Next == \/ ViewCalendar
        \/ AcceptDeny
        \/ CreateSchedule
        \/ Request
        \/ Register
        \/ RescheduleSchedule

                                
                        



=============================================================================
\* Modification History
\* Last modified Thu May 05 14:54:13 BOT 2022 by rosey
\* Created Thu May 05 12:11:23 BOT 2022 by rosey
