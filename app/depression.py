import clips

def calculate_depression_score(answers):
   env = clips.Environment()
   env.reset()

   # Define the symptoms template
   env.build("""
   (deftemplate symptoms
      (slot sleep_issues)
      (slot appetite_changes)
      (slot concentration)
   )
   """)

   # Define the CF values template
   env.build("""
   (deftemplate cf-values
      (slot cf1 (default 0.4))
      (slot cf2 (default 0.2))
      (slot cf3 (default 0.5))
   )
   """)

   env.build("""(deftemplate fired-rules (slot symptom))""")

   env.build("""(deftemplate depression-level (slot level) (slot cf-combined))""")

   env.assert_string("(cf-values)")

   env.build("""
   (defrule check-sleep-issues
      (symptoms (sleep_issues ?answer))
      ?cf <- (cf-values (cf1 ?cf1))
      (not (fired-rules (symptom "sleep_issues")))          ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf1))             ;; Multiply answer by CF value
      (modify ?cf (cf1 ?cf-value))
      (assert (fired-rules (symptom "sleep_issues")))       ;; Mark as processed
   )
   """)

   env.build("""
   (defrule check-appetite-changes
      (symptoms (appetite_changes ?answer))
      ?cf <- (cf-values (cf2 ?cf2))
      (not (fired-rules (symptom "appetite_changes")))      ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf2))             ;; Multiply answer by CF value
      (modify ?cf (cf2 ?cf-value))
      (assert (fired-rules (symptom "appetite_changes")))   ;; Mark as processed
   )
   """)

   env.build("""
   (defrule check-concentration
      (symptoms (concentration ?answer))
      ?cf <- (cf-values (cf3 ?cf3))
      (not (fired-rules (symptom "concentration")))         ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf3))             ;; Multiply answer by CF value
      (modify ?cf (cf3 ?cf-value))
      (assert (fired-rules (symptom "concentration")))      ;; Mark as processed
   )
   """)

   env.build("""
   (defrule final-check
      (cf-values (cf1 ?cf1) (cf2 ?cf2) (cf3 ?cf3))
      =>
      (bind ?cf-old1 (+ ?cf1 (* ?cf2 (- 1 ?cf1))))
      (bind ?cf-combined (+ ?cf-old1 (* ?cf3 (- 1 ?cf-old1))))
      (if (<= ?cf-combined 0) then
         (assert (depression-level (cf-combined ?cf-combined) (level "No Depression")))
      else
         (if (<= ?cf-combined 0.25) then
            (assert (depression-level (cf-combined ?cf-combined) (level "Mild Depression")))
         else
            (if (<= ?cf-combined 0.5) then
               (assert (depression-level (cf-combined ?cf-combined) (level "Moderate Depression")))
            else
               (if (<= ?cf-combined 0.75) then
                  (assert (depression-level (cf-combined ?cf-combined) (level "Severe Depression")))
               else
                  (assert (depression-level (cf-combined ?cf-combined) (level "Highly Severe Depression")))
               )
            )
         )
      )
   )
   """)

   env.build("""
   (defrule result
      (depression-level (level ?level) (cf-combined ?cf-combined))
      =>
      (bind ?percentage (* ?cf-combined 100))
      (halt)
   )
   """)

   env.assert_string(f'(symptoms '
                     f'(sleep_issues {float(answers.get("sleep_issues"))}) '
                     f'(appetite_changes {float(answers.get("appetite_changes"))}) '
                     f'(concentration {float(answers.get("concentration"))}))')

   env.run()

   for fact in env.facts():
      if fact.template.name == 'depression-level':
         severity_level = fact['level']
         certainty_score = f"{(fact['cf-combined'] * 100):.2f}%"

         return severity_level, certainty_score