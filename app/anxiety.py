import clips

def calculate_anxiety_score(answers):
   env = clips.Environment()
   env.reset()

   # Define the symptoms template
   env.build("""
   (deftemplate symptoms
      (slot nervousness)
      (slot restlessness)
      (slot tenseness)
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

   env.build("""(deftemplate anxiety-level (slot level) (slot cf-combined))""")

   env.assert_string("(cf-values)")

   env.build("""
   (defrule check-nervousness
      (symptoms (nervousness ?answer))
      ?cf <- (cf-values (cf1 ?cf1))
      (not (fired-rules (symptom "nervousness")))        ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf1))          ;; Multiply answer by CF value
      (modify ?cf (cf1 ?cf-value))
      (assert (fired-rules (symptom "nervousness")))     ;; Mark as processed
   )
   """)

   env.build("""
   (defrule check-restlessness
      (symptoms (restlessness ?answer))
      ?cf <- (cf-values (cf2 ?cf2))
      (not (fired-rules (symptom "restlessness")))       ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf2))          ;; Multiply answer by CF value
      (modify ?cf (cf2 ?cf-value))
      (assert (fired-rules (symptom "restlessness")))    ;; Mark as processed
   )
   """)

   env.build("""
   (defrule check-tenseness
      (symptoms (tenseness ?answer))
      ?cf <- (cf-values (cf3 ?cf3))
      (not (fired-rules (symptom "tenseness")))          ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf3))          ;; Multiply answer by CF value
      (modify ?cf (cf3 ?cf-value))
      (assert (fired-rules (symptom "tenseness")))       ;; Mark as processed
   )
   """)

   env.build("""
   (defrule final-check
      (cf-values (cf1 ?cf1) (cf2 ?cf2) (cf3 ?cf3))
      =>
      (bind ?cf-old1 (+ ?cf1 (* ?cf2 (- 1 ?cf1))))
      (bind ?cf-combined (+ ?cf-old1 (* ?cf3 (- 1 ?cf-old1))))
      (if (<= ?cf-combined 0) then
         (assert (anxiety-level (cf-combined ?cf-combined) (level "No Anxiety")))
      else
         (if (<= ?cf-combined 0.25) then
            (assert (anxiety-level (cf-combined ?cf-combined) (level "Mild Anxiety")))
         else
            (if (<= ?cf-combined 0.5) then
               (assert (anxiety-level (cf-combined ?cf-combined) (level "Moderate Anxiety")))
            else
               (if (<= ?cf-combined 0.75) then
                  (assert (anxiety-level (cf-combined ?cf-combined) (level "Severe Anxiety")))
               else
                  (assert (anxiety-level (cf-combined ?cf-combined) (level "Highly Severe Anxiety")))
               )
            )
         )
      )
   )
   """)

   env.build("""
   (defrule result
      (anxiety-level (level ?level) (cf-combined ?cf-combined))
      =>
      (bind ?percentage (* ?cf-combined 100))
      (halt)
   )
   """)

   env.assert_string(f'(symptoms '
                     f'(nervousness {float(answers.get("nervousness"))}) '
                     f'(restlessness {float(answers.get("restlessness"))}) '
                     f'(tenseness {float(answers.get("tenseness"))}))')

   env.run()

   for fact in env.facts():
      if fact.template.name == 'anxiety-level':
         severity_level = fact['level']
         certainty_score = f"{(fact['cf-combined'] * 100):.2f}%"

         return severity_level, certainty_score