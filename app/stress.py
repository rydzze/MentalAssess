import clips

def calculate_stress_score(answers):
   env = clips.Environment()
   env.reset()

   # Define the symptoms template
   env.build("""
   (deftemplate symptoms
      (slot overwhelmed)
      (slot irritability)
      (slot tension)
      (slot cope)
      (slot forgetful)
      (slot sensitive)
   )
   """)

   # Define the CF values template - store the CF values for each symptom
   env.build("""
   (deftemplate cf-values
      (slot cf1 (default 0.9))
      (slot cf2 (default 0.6))
      (slot cf3 (default 0.7))
      (slot cf4 (default 0.3))
      (slot cf5 (default 0.2))
      (slot cf6 (default 0.4))
   )
   """)

   # Define the fired rules template - track rules that have fired, avoid re-firing
   env.build("""(deftemplate fired-rules (slot symptom))""")

   # Define the depression level template - store the severity level and combined CF values for return value
   env.build("""(deftemplate stress-level (slot level) (slot cf-combine))""")

   env.assert_string("(cf-values)")

   # Do you feel overwhelmed frequently?
   env.build("""
   (defrule check-overwhelmed
      (symptoms (overwhelmed ?answer))
      ?cf <- (cf-values (cf1 ?cf1))
      (not (fired-rules (symptom "overwhelmed")))        ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf1))          ;; Multiply answer by CF value
      (modify ?cf (cf1 ?cf-value))
      (assert (fired-rules (symptom "overwhelmed")))     ;; Mark as fired
   )
   """)

   # Do you feel irritable or impatient often?
   env.build("""
   (defrule check-irritability
      (symptoms (irritability ?answer))
      ?cf <- (cf-values (cf2 ?cf2))
      (not (fired-rules (symptom "irritability")))       ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf2))          ;; Multiply answer by CF value
      (modify ?cf (cf2 ?cf-value))
      (assert (fired-rules (symptom "irritability")))    ;; Mark as fired
   )
   """)

   # Do you experience headaches or physical tension?
   env.build("""
   (defrule check-tension
      (symptoms (tension ?answer))
      ?cf <- (cf-values (cf3 ?cf3))
      (not (fired-rules (symptom "tension")))            ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf3))          ;; Multiply answer by CF value
      (modify ?cf (cf3 ?cf-value))
      (assert (fired-rules (symptom "tension")))         ;; Mark as fired
   )
   """)

   # Felt that you could NOT cope with all the things you had to do?
   env.build("""
   (defrule check-cope
      (symptoms (cope ?answer))
      ?cf <- (cf-values (cf4 ?cf4))
      (not (fired-rules (symptom "cope")))               ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf4))          ;; Multiply answer by CF value
      (modify ?cf (cf4 ?cf-value))
      (assert (fired-rules (symptom "cope")))            ;; Mark as fired
   )
   """)

   # Do you experience memory problems or difficulty making decisions?
   env.build("""
   (defrule check-forgetful
      (symptoms (forgetful ?answer))
      ?cf <- (cf-values (cf5 ?cf5))
      (not (fired-rules (symptom "forgetful")))          ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf5))          ;; Multiply answer by CF value
      (modify ?cf (cf5 ?cf-value))
      (assert (fired-rules (symptom "forgetful")))       ;; Mark as fired
   )
   """)

   # Do you found yourself sensitive to noise or distractions?
   env.build("""
   (defrule check-sensitive
      (symptoms (sensitive ?answer))
      ?cf <- (cf-values (cf6 ?cf6))
      (not (fired-rules (symptom "sensitive")))          ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf6))          ;; Multiply answer by CF value
      (modify ?cf (cf6 ?cf-value))
      (assert (fired-rules (symptom "sensitive")))       ;; Mark as fired
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
         (assert (stress-level (cf-combine ?cf-combine-5) (level "No Stress")))
      else
         (if (<= ?cf-combine-5 0.25) then
            (assert (stress-level (cf-combine ?cf-combine-5) (level "Mild Stress")))
         else
            (if (<= ?cf-combine-5 0.5) then
               (assert (stress-level (cf-combine ?cf-combine-5) (level "Moderate Stress")))
            else
               (if (<= ?cf-combine-5 0.75) then
                  (assert (stress-level (cf-combine ?cf-combine-5) (level "Severe Stress")))
               else
                  (assert (stress-level (cf-combine ?cf-combine-5) (level "Highly Severe Stress")))
               )
            )
         )
      )
   )
   """)

   # Return the severity level and certainty score in percentage
   env.build("""
   (defrule result
      (stress-level (level ?level) (cf-combine ?cf-combine-5))
      =>
      (bind ?percentage (* ?cf-combine-5 100))
      (halt)
   )
   """)

   env.assert_string(f'(symptoms '
                     f'(overwhelmed {float(answers.get("overwhelmed"))}) '
                     f'(irritability {float(answers.get("irritability"))}) '
                     f'(tension {float(answers.get("tension"))}) '
                     f'(cope {float(answers.get("cope"))}) '
                     f'(forgetful {float(answers.get("forgetful"))}) '
                     f'(sensitive {float(answers.get("sensitive"))}))')

   env.run()

   for fact in env.facts():
      if fact.template.name == 'stress-level':
         severity_level = fact['level']
         certainty_score = f"{(fact['cf-combine'] * 100):.2f}%"

         return severity_level, certainty_score