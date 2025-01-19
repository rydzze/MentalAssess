import clips

def calculate_depression_score(answers):
   env = clips.Environment()
   env.reset()

   # Define the symptoms template
   env.build("""
   (deftemplate symptoms
      (slot sleep_issues)
      (slot energy)
      (slot appetite)
      (slot concentration)
      (slot behaviour)
      (slot emotion)
   )
   """)

   # Define the CF values template - store the CF values for each symptom
   env.build("""
   (deftemplate cf-values
      (slot cf1 (default 0.1))
      (slot cf2 (default 0.8))
      (slot cf3 (default 0.6))
      (slot cf4 (default 0.4))
      (slot cf5 (default 0.3))
      (slot cf6 (default 1.0))
   )
   """)

   # Define the fired rules template - track rules that have fired, avoid re-firing
   env.build("""(deftemplate fired-rules (slot symptom))""")

   # Define the depression level template - store the severity level and combined CF values for return value
   env.build("""(deftemplate depression-level (slot level) (slot cf-combine))""")

   env.assert_string("(cf-values)")

   # # How often have you had trouble sleeping over the past two weeks?
   env.build("""
   (defrule check-sleep-issues
      (symptoms (sleep_issues ?answer))
      ?cf <- (cf-values (cf1 ?cf1))
      (not (fired-rules (symptom "sleep_issues")))          ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf1))             ;; Multiply answer by CF value
      (modify ?cf (cf1 ?cf-value))
      (assert (fired-rules (symptom "sleep_issues")))       ;; Mark as fired
   )
   """)

   # How much have you felt a lack of energy over the last two weeks?
   env.build("""
   (defrule check-energy
      (symptoms (energy ?answer))
      ?cf <- (cf-values (cf2 ?cf2))
      (not (fired-rules (symptom "energy")))                ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf2))             ;; Multiply answer by CF value
      (modify ?cf (cf2 ?cf-value))
      (assert (fired-rules (symptom "energy")))             ;; Mark as fired
   )
   """)

   # How much have you noticed changes in your appetite over the last two weeks?
   env.build("""
   (defrule check-appetite
      (symptoms (appetite ?answer))
      ?cf <- (cf-values (cf3 ?cf3))
      (not (fired-rules (symptom "appetite")))              ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf3))             ;; Multiply answer by CF value
      (modify ?cf (cf3 ?cf-value))
      (assert (fired-rules (symptom "appetite")))           ;; Mark as fired
   )
   """)

   # To what extent have you had difficulty concentrating over the last two weeks?
   env.build("""
   (defrule check-concentration
      (symptoms (concentration ?answer))
      ?cf <- (cf-values (cf4 ?cf4))
      (not (fired-rules (symptom "concentration")))         ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf4))             ;; Multiply answer by CF value
      (modify ?cf (cf4 ?cf-value))
      (assert (fired-rules (symptom "concentration")))      ;; Mark as fired
   )
   """)

   # How much have you felt passive or lacked motivation to engage in activities over the last two weeks?
   env.build("""
   (defrule check-behaviour
      (symptoms (behaviour ?answer))
      ?cf <- (cf-values (cf5 ?cf5))
      (not (fired-rules (symptom "behaviour")))             ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf5))             ;; Multiply answer by CF value
      (modify ?cf (cf5 ?cf-value))
      (assert (fired-rules (symptom "behaviour")))          ;; Mark as fired
   )
   """)

   # Can you rate how much you felt sad in the past two weeks?
   env.build("""
   (defrule check-emotion
      (symptoms (emotion ?answer))
      ?cf <- (cf-values (cf6 ?cf6))
      (not (fired-rules (symptom "emotion")))               ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf6))             ;; Multiply answer by CF value
      (modify ?cf (cf6 ?cf-value))
      (assert (fired-rules (symptom "emotion")))            ;; Mark as fired
   )
   """)

   # Combine the CF values to calculate the overall CF value
   env.build("""
   (defrule calculate-cf-combine
      (cf-values (cf1 ?cf1) (cf2 ?cf2) (cf3 ?cf3) (cf4 ?cf4) (cf5 ?cf5) (cf6 ?cf6))
      =>
      (bind ?cf-combine-1 (+ ?cf1 (* ?cf2 (- 1 ?cf1))))
      (bind ?cf-combine-2 (+ ?cf-combine-1 (* ?cf3 (- 1 ?cf-combine-1))))
      (bind ?cf-combine-3 (+ ?cf-combine-2 (* ?cf4 (- 1 ?cf-combine-2))))
      (bind ?cf-combine-4 (+ ?cf-combine-3 (* ?cf5 (- 1 ?cf-combine-3))))
      (bind ?cf-combine-5 (+ ?cf-combine-4 (* ?cf6 (- 1 ?cf-combine-4))))
      (if (<= ?cf-combine-5 0) then
         (assert (depression-level (cf-combine ?cf-combine-5) (level "No Depression")))
      else
         (if (<= ?cf-combine-5 0.25) then
            (assert (depression-level (cf-combine ?cf-combine-5) (level "Mild Depression")))
         else
            (if (<= ?cf-combine-5 0.5) then
               (assert (depression-level (cf-combine ?cf-combine-5) (level "Moderate Depression")))
            else
               (if (<= ?cf-combine-5 0.75) then
                  (assert (depression-level (cf-combine ?cf-combine-5) (level "Severe Depression")))
               else
                  (assert (depression-level (cf-combine ?cf-combine-5) (level "Highly Severe Depression")))
               )
            )
         )
      )
   )
   """)

   # Return the severity level and certainty score in percentage
   env.build("""
   (defrule result
      (depression-level (level ?level) (cf-combine ?cf-combine-5))
      =>
      (bind ?percentage (* ?cf-combine-5 100))
      (halt)
   )
   """)

   env.assert_string(f'(symptoms '
                     f'(sleep_issues {float(answers.get("sleep_issues"))}) '
                     f'(energy {float(answers.get("energy"))}) '
                     f'(appetite {float(answers.get("appetite"))}) '
                     f'(concentration {float(answers.get("concentration"))}) '
                     f'(behaviour {float(answers.get("behaviour"))}) '
                     f'(emotion {float(answers.get("emotion"))}))')

   env.run()

   for fact in env.facts():
      if fact.template.name == 'depression-level':
         severity_level = fact['level']
         certainty_score = f"{(fact['cf-combine'] * 100):.2f}%"

         return severity_level, certainty_score