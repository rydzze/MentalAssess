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

   # Define the CF values template
   env.build("""
   (deftemplate cf-values
      (slot cf1 (default 0.1))
      (slot cf2 (default 0.8))
      (slot cf3 (default 0.7))
      (slot cf4 (default 0.5))
      (slot cf5 (default 0.2))
      (slot cf6 (default 1.0))
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
   (defrule check-energy
      (symptoms (energy ?answer))
      ?cf <- (cf-values (cf2 ?cf2))
      (not (fired-rules (symptom "energy")))                ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf2))             ;; Multiply answer by CF value
      (modify ?cf (cf2 ?cf-value))
      (assert (fired-rules (symptom "energy")))             ;; Mark as processed
   )
   """)

   env.build("""
   (defrule check-appetite
      (symptoms (appetite ?answer))
      ?cf <- (cf-values (cf3 ?cf3))
      (not (fired-rules (symptom "appetite")))              ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf3))             ;; Multiply answer by CF value
      (modify ?cf (cf3 ?cf-value))
      (assert (fired-rules (symptom "appetite")))           ;; Mark as processed
   )
   """)

   env.build("""
   (defrule check-concentration
      (symptoms (concentration ?answer))
      ?cf <- (cf-values (cf4 ?cf4))
      (not (fired-rules (symptom "concentration")))         ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf4))             ;; Multiply answer by CF value
      (modify ?cf (cf4 ?cf-value))
      (assert (fired-rules (symptom "concentration")))      ;; Mark as processed
   )
   """)

   env.build("""
   (defrule check-behaviour
      (symptoms (behaviour ?answer))
      ?cf <- (cf-values (cf5 ?cf5))
      (not (fired-rules (symptom "behaviour")))             ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf5))             ;; Multiply answer by CF value
      (modify ?cf (cf5 ?cf-value))
      (assert (fired-rules (symptom "behaviour")))          ;; Mark as processed
   )
   """)

   env.build("""
   (defrule check-emotion
      (symptoms (emotion ?answer))
      ?cf <- (cf-values (cf6 ?cf6))
      (not (fired-rules (symptom "emotion")))               ;; Ensure the rule only fires once
      =>
      (bind ?cf-value (* (float ?answer) ?cf6))             ;; Multiply answer by CF value
      (modify ?cf (cf6 ?cf-value))
      (assert (fired-rules (symptom "emotion")))            ;; Mark as processed
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
                     f'(energy {float(answers.get("energy"))}) '
                     f'(appetite {float(answers.get("appetite"))}) '
                     f'(concentration {float(answers.get("concentration"))}))'
                     f'(behaviour {float(answers.get("behaviour"))}) '
                     f'(emotion {float(answers.get("emotion"))}) ')

   env.run()

   for fact in env.facts():
      if fact.template.name == 'depression-level':
         severity_level = fact['level']
         certainty_score = f"{(fact['cf-combined'] * 100):.2f}%"

         return severity_level, certainty_score