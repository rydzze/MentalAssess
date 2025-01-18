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
      (slot panicky)
      (slot overthinking)
      (slot shortbreath)
   )
   """)

   # Define the CF values template - store the CF values for each symptom
   env.build("""
   (deftemplate cf-values
      (slot cf1 (default 0.7))
      (slot cf2 (default 0.2))
      (slot cf3 (default 0.6))
      (slot cf4 (default 0.4))
      (slot cf5 (default 0.8))
      (slot cf6 (default 0.3))
   )
   """)

   # Define the fired rules template - track rules that have fired, avoid re-firing
   env.build("""(deftemplate fired-rules (slot symptom))""")

   # Define the depression level template - store the severity level and combined CF values for return value
   env.build("""(deftemplate anxiety-level (slot level) (slot cf-combined))""")

   env.assert_string("(cf-values)")

   # Do you feel nervous frequently?
   env.build("""
   (defrule check-nervousness
      (symptoms (nervousness ?answer))
      ?cf <- (cf-values (cf1 ?cf1))
      (not (fired-rules (symptom "nervousness")))        ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf1))          ;; Multiply answer by CF value
      (modify ?cf (cf1 ?cf-value))
      (assert (fired-rules (symptom "nervousness")))     ;; Mark as fired
   )
   """)

   # Do you feel restless or uneasy?
   env.build("""
   (defrule check-restlessness
      (symptoms (restlessness ?answer))
      ?cf <- (cf-values (cf2 ?cf2))
      (not (fired-rules (symptom "restlessness")))       ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf2))          ;; Multiply answer by CF value
      (modify ?cf (cf2 ?cf-value))
      (assert (fired-rules (symptom "restlessness")))    ;; Mark as fired
   )
   """)

   # Do you feel tense or unable to relax?
   env.build("""
   (defrule check-tenseness
      (symptoms (tenseness ?answer))
      ?cf <- (cf-values (cf3 ?cf3))
      (not (fired-rules (symptom "tenseness")))          ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf3))          ;; Multiply answer by CF value
      (modify ?cf (cf3 ?cf-value))
      (assert (fired-rules (symptom "tenseness")))       ;; Mark as fired
   )
   """)

   # Do you experience sudden feelings of panic or fear without an obvious reason?
   env.build("""
   (defrule check-panicky
      (symptoms (panicky ?answer))
      ?cf <- (cf-values (cf4 ?cf4))
      (not (fired-rules (symptom "panicky")))            ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf4))          ;; Multiply answer by CF value
      (modify ?cf (cf4 ?cf-value))
      (assert (fired-rules (symptom "panicky")))         ;; Mark as fired
   )
   """)

   # Do you find yourself overthinking or dwelling on things that might go wrong?
   env.build("""
   (defrule check-overthinking
      (symptoms (overthinking ?answer))
      ?cf <- (cf-values (cf5 ?cf5))
      (not (fired-rules (symptom "overthinking")))       ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf5))          ;; Multiply answer by CF value
      (modify ?cf (cf5 ?cf-value))
      (assert (fired-rules (symptom "overthinking")))    ;; Mark as fired
   )
   """)

   # Have you ever experienced shortness of breath lately?
   env.build("""
   (defrule check-shortbreath
      (symptoms (shortbreath ?answer))
      ?cf <- (cf-values (cf6 ?cf6))
      (not (fired-rules (symptom "shortbreath")))        ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf6))          ;; Multiply answer by CF value
      (modify ?cf (cf6 ?cf-value))
      (assert (fired-rules (symptom "shortbreath")))     ;; Mark as fired
   )
   """)

   env.build("""
   (defrule final-check
      (cf-values (cf1 ?cf1) (cf2 ?cf2) (cf3 ?cf3) (cf4 ?cf4) (cf5 ?cf5) (cf6 ?cf6))
      =>
      (bind ?cf-old1 (+ ?cf1 (* ?cf2 (- 1 ?cf1))))
      (bind ?cf-old2 (+ ?cf-old1 (* ?cf3 (- 1 ?cf-old1))))
      (bind ?cf-old3 (+ ?cf-old2 (* ?cf4 (- 1 ?cf-old2))))
      (bind ?cf-old4 (+ ?cf-old3 (* ?cf5 (- 1 ?cf-old3))))
      (bind ?cf-combined (+ ?cf-old4 (* ?cf6 (- 1 ?cf-old4))))
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
                     f'(tenseness {float(answers.get("tenseness"))}) '
                     f'(panicky {float(answers.get("panicky"))}) '
                     f'(overthinking {float(answers.get("overthinking"))}) '
                     f'(shortbreath {float(answers.get("shortbreath"))}))')

   env.run()

   for fact in env.facts():
      if fact.template.name == 'anxiety-level':
         severity_level = fact['level']
         certainty_score = f"{(fact['cf-combined'] * 100):.2f}%"

         return severity_level, certainty_score