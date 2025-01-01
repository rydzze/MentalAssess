import clips

def calculate_stress_score(answers):
    env = clips.Environment()
    env.reset()

    env.build("""
    (deftemplate questionnaire
       (slot overwhelmed)
       (slot irritability)
       (slot tension)
    )
    """)

    env.build("""
    (deftemplate stress-value
       (slot value)
       (slot cf)
    )
    """)

    env.build("""
    (deftemplate cf-values
       (slot cf1 (default 0))
       (slot cf2 (default 0))
       (slot cf3 (default 0))
    )
    """)

    env.assert_string("(cf-values)")

    env.build("""
    (defrule check-overwhelmed
       (questionnaire (overwhelmed ?answer))
       ?cf <- (cf-values (cf1 ?cf1))
       =>
       (if (eq ?answer "yes") then
          (modify ?cf (cf1 0.75))
       else
          (modify ?cf (cf1 0.25))
       )
    )
    """)

    env.build("""
    (defrule check-irritability
       (questionnaire (irritability ?answer))
       ?cf <- (cf-values (cf2 ?cf2))
       =>
       (if (eq ?answer "yes") then
          (modify ?cf (cf2 0.80))
       else
          (modify ?cf (cf2 0.20))
       )
    )
    """)

    env.build("""
    (defrule check-tension
       (questionnaire (tension ?answer))
       ?cf <- (cf-values (cf3 ?cf3))
       =>
       (if (eq ?answer "yes") then
          (modify ?cf (cf3 0.95))
       else
          (modify ?cf (cf3 0.05))
       )
    )
    """)

    env.build("""
    (defrule final-check
       (cf-values (cf1 ?cf1) (cf2 ?cf2) (cf3 ?cf3))
       =>
       (bind ?total (+ ?cf1 ?cf2 ?cf3))
       (bind ?average (/ ?total 3))
       (if (<= ?average 0.25) then
          (assert (stress-value (cf ?average) (value "No Stress")))
       else
          (if (<= ?average 0.5) then
             (assert (stress-value (cf ?average) (value "Mild Stress")))
          else
             (if (<= ?average 0.75) then
                (assert (stress-value (cf ?average) (value "Moderate Stress")))
             else
                (assert (stress-value (cf ?average) (value "Severe Stress")))
             )
          )
       )
    )
    """)

    env.build("""
    (defrule final-value
       (stress-value (value ?level) (cf ?certainty))
       =>
       (bind ?percentage (* ?certainty 100))
       (halt)
    )
    """)

    env.assert_string(f'(questionnaire (overwhelmed "{answers.get("overwhelmed")}") (irritability "{answers.get("irritability")}") (tension "{answers.get("tension")}") )')

    env.run()

    for fact in env.facts():
        if fact.template.name == 'stress-value':
            severity_level = fact['value']
            certainty_factor = f"{(fact['cf'] * 100):.2f}%"

            return severity_level, certainty_factor