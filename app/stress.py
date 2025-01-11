import clips

def calculate_stress_score(answers):
    env = clips.Environment()
    env.reset()

    env.build("""
    (deftemplate questionnaire
       (slot overwhelmed)
       (slot irritability)
       (slot tension)
       (slot lonely)
       (slot forgetful)
       (slot unhealthy)
       (slot uncontrolled)
       (slot stressful)
       (slot lost_interest)
       (slot sensitive)
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
       (slot cf4 (default 0))
       (slot cf5 (default 0))
       (slot cf6 (default 0))
       (slot cf7 (default 0))
       (slot cf8 (default 0))
       (slot cf9 (default 0))
       (slot cf10 (default 0))
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
    (defrule check-lonely
       (questionnaire (lonely ?answer))
       ?cf <- (cf-values (cf4 ?cf4))
       =>
       (if (eq ?answer "yes") then
          (modify ?cf (cf4 0.95))
       else
          (modify ?cf (cf4 0.05))
       )
    )
    """)

    env.build("""
    (defrule check-forgetful
       (questionnaire (forgetful ?answer))
       ?cf <- (cf-values (cf5 ?cf5))
       =>
       (if (eq ?answer "yes") then
          (modify ?cf (cf5 0.95))
       else
          (modify ?cf (cf5 0.05))
       )
    )
    """)

    env.build("""
    (defrule check-unhealthy
       (questionnaire (unhealthy ?answer))
       ?cf <- (cf-values (cf6 ?cf6))
       =>
       (if (eq ?answer "yes") then
          (modify ?cf (cf6 0.95))
       else
          (modify ?cf (cf6 0.05))
       )
    )
    """)

    env.build("""
    (defrule check-uncontrolled
       (questionnaire (uncontrolled ?answer))
       ?cf <- (cf-values (cf7 ?cf7))
       =>
       (if (eq ?answer "yes") then
          (modify ?cf (cf7 0.95))
       else
          (modify ?cf (cf7 0.05))
       )
    )
    """)

    env.build("""
    (defrule check-stressful
       (questionnaire (stressful ?answer))
       ?cf <- (cf-values (cf8 ?cf8))
       =>
       (if (eq ?answer "yes") then
          (modify ?cf (cf8 0.95))
       else
          (modify ?cf (cf8 0.05))
       )
    )
    """)

    env.build("""
    (defrule check-lost_interest
       (questionnaire (lost_interest ?answer))
       ?cf <- (cf-values (cf9 ?cf9))
       =>
       (if (eq ?answer "yes") then
          (modify ?cf (cf9 0.95))
       else
          (modify ?cf (cf9 0.05))
       )
    )
    """)

    env.build("""
    (defrule check-sensitive
       (questionnaire (sensitive ?answer))
       ?cf <- (cf-values (cf10 ?cf10))
       =>
       (if (eq ?answer "yes") then
          (modify ?cf (cf10 0.95))
       else
          (modify ?cf (cf10 0.05))
       )
    )
    """)

    env.build("""
    (defrule final-check
       (cf-values (cf1 ?cf1) (cf2 ?cf2) (cf3 ?cf3) (cf4 ?cf4) (cf5 ?cf5) (cf6 ?cf6) (cf7 ?cf7) (cf8 ?cf8) (cf9 ?cf9) (cf10 ?cf10))
       =>
       (bind ?total (+ ?cf1 ?cf2 ?cf3 ?cf4 ?cf5 ?cf6 ?cf7 ?cf8 ?cf9 ?cf10))
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

    env.assert_string(f'(questionnaire (overwhelmed "{answers.get("overwhelmed")}") (irritability "{answers.get("irritability")}") (tension "{answers.get("tension")}") (lonely "{answers.get("lonely")}") (forgetful "{answers.get("forgetful")}") (unhealthy "{answers.get("unhealthy")}") (uncontrolled "{answers.get("uncontrolled")}") (stressful "{answers.get("stressful")}") (lost_interest "{answers.get("lost_interest")}") (sensitive "{answers.get("sensitive")}"))')

    env.run()

    for fact in env.facts():
        if fact.template.name == 'stress-value':
            severity_level = fact['value']
            certainty_factor = f"{(fact['cf'] * 100):.2f}%"

            return severity_level, certainty_factor