try:
   ...
except FirstException:
   handle_first_one()

except SecondException:
   handle_second_one()

except (ThirdException, FourthException, FifthException) as e:
   handle_either_of_3rd_4th_or_5th()

except Exception:
   handle_all_other_exceptions()
