# 1. Magnetostatic fundamentals

## 1.1 Assumptions and their limits

The standard surgical-robotics model makes four reductions:

1. currents and magnet motion are slow enough that a magnetostatic approximation is adequate;
2. the anatomy and workspace have relative permeability close to one;
3. the permanent magnets are rigid dipoles with constant moment magnitude;
4. the evaluation point lies far enough from each magnet for a point-dipole approximation.

These are modelling assumptions, not universal truths. The dipole approximation can be excellent several characteristic magnet lengths away and poor near a large EPM. Near-field clinical systems should compare the dipole model with an analytic finite-magnet model, measured maps, or finite-element analysis.

Outside current-carrying and magnetic material, Maxwell's magnetostatic constraints are

\[
\nabla\cdot\mathbf B=0,\qquad \nabla\times\mathbf B=\mathbf 0.
\]

Consequences used in actuation design are:

- the \(3\times3\) field-gradient matrix \(\nabla\mathbf B\) is trace-free;
- in a current-free region it is symmetric;
- therefore it has five independent components, not nine;
- a local magnetic command can be represented by three field plus five gradient components.

This is why multi-actuator systems are commonly analyzed through an eight-component magnetic control vector rather than twelve arbitrary field-and-gradient values.

## 1.2 Field of a point dipole

Let \(\mathbf r=\mathbf p_I-\mathbf p_E\) point from the EPM source to the IPM receiver, \(r=\|\mathbf r\|\), and \(\hat{\mathbf r}=\mathbf r/r\). The EPM field at the IPM is

\[
\mathbf B_E(\mathbf r)
=\frac{\mu_0}{4\pi r^3}
\left(3\hat{\mathbf r}\hat{\mathbf r}^{\!T}-I_3\right)\mathbf m_E.
\]

Define \(D(\hat{\mathbf r})=3\hat{\mathbf r}\hat{\mathbf r}^{T}-I_3\). Then \(\mathbf B_E=c_D D\mathbf m_E/r^3\), where \(c_D=\mu_0/(4\pi)\).

The dipole moment of a uniformly magnetized magnet can be estimated by

\[
\mathbf m\approx \mathbf M V,
\]

where \(\mathbf M\) is magnetization and \(V\) is volume. In experimental work, use the manufacturer's residual flux density only with a geometry/material model or identify \(\mathbf m\) from field measurements; treating \(m=B_rV/\mu_0\) as exact hides demagnetization effects.

## 1.3 Energy and torque

The potential energy of the IPM in the EPM field is

\[
U_m=-\mathbf m_I^T\mathbf B_E.
\]

An infinitesimal rotation \(\delta\boldsymbol\theta\) changes \(\mathbf m_I\) by \(\delta\mathbf m_I=\delta\boldsymbol\theta\times\mathbf m_I\). Equating \(\delta U=-\boldsymbol\tau_m^T\delta\boldsymbol\theta\) gives

\[
\boxed{\boldsymbol\tau_m=\mathbf m_I\times\mathbf B_E.}
\]

Torque aligns the internal magnet with the local field. Rotation about the magnetization axis is not magnetically observable or controllable for an axially symmetric dipole; this is the basic reason a single uniform-field command gives two orientational degrees of authority rather than three.

## 1.4 Force from energy

For constant \(\mathbf m_I\),

\[
\mathbf F_m=-\nabla_{\mathbf r}U_m
=\nabla_{\mathbf r}(\mathbf m_I^T\mathbf B_E)
=(\nabla\mathbf B_E)^T\mathbf m_I.
\]

Because \(\nabla\times\mathbf B=0\) makes \(\nabla\mathbf B\) symmetric in the local source-free region, this is also often written \((\mathbf m_I\cdot\nabla)\mathbf B_E\).

Differentiating the dipole field yields the closed form

\[
\boxed{
\mathbf F_m=
\frac{3\mu_0}{4\pi r^4}
\left[
(\mathbf m_E^T\hat{\mathbf r})\mathbf m_I
+(\mathbf m_I^T\hat{\mathbf r})\mathbf m_E
+(\mathbf m_E^T\mathbf m_I)\hat{\mathbf r}
-5(\mathbf m_E^T\hat{\mathbf r})(\mathbf m_I^T\hat{\mathbf r})\hat{\mathbf r}
\right].}
\]

With \(\mathbf m_E=m_E\hat{\mathbf e}_E\), \(\mathbf m_I=m_I\hat{\mathbf e}_I\), and \(Z=I_3-5\hat{\mathbf r}\hat{\mathbf r}^T\), the same result is

\[
\mathbf F_m=\frac{3\lambda}{r}
\left[
\hat{\mathbf e}_I\hat{\mathbf e}_E^T
+\hat{\mathbf e}_E\hat{\mathbf e}_I^T
+(\hat{\mathbf e}_I^TZ\hat{\mathbf e}_E)I_3
\right]\hat{\mathbf r},
\quad
\lambda=\frac{\mu_0m_Em_I}{4\pi r^3}.
\]

The cross term contains both unit magnet directions. Notebook 01 demonstrates this independently through an energy-gradient calculation.

## 1.5 Scaling laws that matter in surgery

For fixed moments and orientation,

\[
\|\mathbf B\|\propto r^{-3},\qquad
\|\boldsymbol\tau_m\|\propto r^{-3},\qquad
\|\mathbf F_m\|\propto r^{-4}.
\]

Increasing the skin-to-target distance from 100 mm to 150 mm reduces dipole field and torque to about \((100/150)^3=0.296\) and force to \((100/150)^4=0.198\) of their original values. Human-scale depth is therefore a first-order design variable, not merely a larger benchtop workspace.

## 1.6 Dimensional and physical checks

Every implementation should pass these tests:

| Check | Expected result |
|---|---|
| Units of \(B\) | tesla |
| Units of \(F\) | newton |
| Units of \(\tau\) | newton metre |
| \(\mathbf r\to-\mathbf r\) | dipole field unchanged, receiver force changes sign |
| \(\mathbf m_I\parallel\mathbf B\) | torque is zero |
| Exchange source and receiver positions | forces are equal and opposite under the same global geometry |
| Central energy difference | \(-\nabla U\) matches closed-form force |
| Translation of both magnets together | wrench unchanged |

## 1.7 Beyond the point dipole

Use a higher-fidelity model when one or more of the following are true:

- EPM–IPM separation is comparable to magnet dimensions;
- the EPM has an unusual aspect ratio or a return yoke;
- multiple magnets interact strongly;
- nearby ferromagnetic surgical tools distort the field;
- force error, not just field-direction error, affects tissue safety;
- optimization places the actuator repeatedly at the boundary of dipole validity.

A practical hierarchy is: point dipole for analysis and initialization; closed-form finite cylinder/cuboid or calibrated field map for control; finite-element analysis for design; empirical residual correction for the final system.
