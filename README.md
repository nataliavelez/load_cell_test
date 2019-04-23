# Experiment: Pulling a rigged box
Natalia Vélez, Xi Jia Zhou, Hyowon Gweon
April 2019

In this experiment, children will be introduced to a *strong* or *weak* agent,
and they will observe as the agent either *succeeds* or *fails* to lift a box.
Children will then have the opportunity to pull the box themselves.
Unbeknownst to the children, the box is bolted to the table, so they will fail
to pull it. Inside the box, we have installed a load cell and HX711 amplifier
that measure the force children apply to pull the box.

The main hypothesis tested here is that children will use the observations
of the other agents' actions to infer the weight of a box and, consequently,
how much force they should apply to successfully move the box.

In this folder:

* `data`: Data from each recording session, saved as csv files
* `arduino_send`: Arduino sketch that transmits sensor data
* `run_experiment.py`: Main script, saves sensor data.
