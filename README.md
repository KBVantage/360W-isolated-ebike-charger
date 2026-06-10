# 360W E-Bike Charger

A high-efficiency isolated AC-DC charger designed for a 24V 100Ah LiFePO4 battery pack used in e-bike applications.  
The charger accepts universal single-phase AC input from 110–230 Vrms, performs EMC filtering and rectification, converts the power through an LLC resonant stage, and regulates battery charging using CC/CV control coordinated with the BMS.

<img width="1533" height="678" alt="image" src="https://github.com/user-attachments/assets/bf468802-4845-4ba2-988b-6fb6fd7760fc" />

The design achieves up to 24V at 15A peak output current with approximately 94% efficiency at the operating point.  
The control and monitoring architecture uses an STM32L0 microcontroller, while Python scripts were used to support test automation and measurement analysis.  
Design capture was done in Altium Designer, circuit verification was supported with LTspice, and firmware development used STM IDE.

---

## Overview

This project documents the complete development flow of a 360W isolated e-bike charger, from initial specification through schematic design, simulation, PCB layout, validation, and thermal testing.  
The architecture was chosen to deliver efficient battery charging for a 24V LiFePO4 pack while maintaining isolation, safety, EMC performance, and reliable current regulation.  
The battery charging profile follows the CCCV method through communication with the BMS, allowing the charger to gradually increase current and then transition into constant-voltage regulation when the battery approaches its target voltage.

---

## Design Flow

This repository is organized to reflect the engineering process used to develop the charger:

1. Define specifications and operating targets.
2. Build the system block diagram.
3. Select and size power-stage components.
4. Simulate critical circuits in LTspice.
5. Capture the schematic and PCB in Altium Designer.
6. Develop embedded control and measurement firmware in STM32 IDE.
7. Assemble the PCB and generate manufacturing files.
8. Validate the prototype with bench testing and thermal measurements.
9. Analyze measured data with Python automation.

This structure is intended to show not only the final design, but also the reasoning behind each stage of the implementation.

---

## Specifications

### Input
- 110–230 Vrms, single-phase AC input.
- EMC filter at the input stage.
- Common-mode filtering for conducted noise reduction.
- 10A fuse protection.
- Bulk capacitance after rectification.
- Bridge diode rectifier.

### Power conversion
- LLC resonant converter for isolated power transfer.
- High-voltage primary MOSFETs rated 650V, TO-247 super-junction devices.
- Transformer optimized for the required power and isolation.
- Synchronous rectification on the secondary side with SR controller.
- 60V LFPAK56 MOSFETs on the secondary rectifier.

### Output and battery interface
- 24V LiFePO4 battery pack, 100Ah.
- BMS communication for CCCV charging control.
- Peak output current: 15A.

### Control and low-voltage power
- STM32L0 microcontroller for system monitoring and charge control.
- 12V, 5V, and 3.3V rails generated from the battery side using buck regulators and LDOs.
- Isolation used where required for safety and signal integrity.

---

## System Architecture

The charger begins with the AC input stage, where EMI and common-mode filtering reduce noise before the line is protected by a fuse and rectified by a bridge diode stage.  
The rectified DC bus is smoothed with bulk capacitance and then processed by the LLC resonant converter, which provides efficient isolated power transfer at 360W.  
The transformer transfers energy across the isolation barrier, and synchronous rectification on the secondary side improves efficiency compared to passive rectification, especially at higher current.

The battery-side control system communicates with the BMS to coordinate CCCV charging.  
Current and voltage are measured at multiple stages of the power path so the charger can regulate the output safely and transition smoothly through the charging phases.  
Low-voltage housekeeping supplies are derived from the battery side using buck converters and LDOs to power the MCU and auxiliary circuitry.

---

## Component Selection

### Input stage
The fuse was selected to protect the charger against abnormal current conditions and fault scenarios.  
The EMC filter and common-mode choke were chosen to reduce conducted emissions and improve input-side noise suppression.  
Bulk capacitance was sized to support the rectified bus ripple and maintain stable energy storage after the bridge rectifier.

### Primary power stage
The primary switches are 650V TO-247 super-junction MOSFETs selected for voltage margin, thermal robustness, and availability during early hardware bring-up.  
This stage is planned for a later GaN update to further reduce switching losses and improve power density.  
The LLC topology was selected because it offers soft-switching behavior and high efficiency at medium power levels.

### Secondary power stage
The synchronous rectifier uses 60V LFPAK56 MOSFETs chosen for low conduction loss and compact package size.  
The SR controller manages timing to reduce diode-like losses on the secondary side and improve thermal performance.  
This is especially useful in a 24V, 15A charger where secondary conduction losses become significant.

### Control and sensing
The STM32L0 was selected for its low-power operation, compact integration, and flexible peripheral set.  
It supports the measurement, sequencing, communication, and supervisory logic needed for a charger platform.  
Its ultra-low-power characteristics also make it suitable for auxiliary management and standby behavior [web:117][web:123].

---

## Charging Method

The charger supports CCCV charging by communicating with the BMS (19 V to 29.2 V according to the battery charging profile).  
During constant-current operation, the output current is regulated to charge the battery quickly and safely.  
As the battery voltage rises, the charger transitions into constant-voltage mode, gradually reducing current while maintaining the target voltage until the battery is nearly full.

This approach is well-suited to LiFePO4 chemistry because the battery benefits from controlled charging and stable voltage limits.  
Measurement of current and voltage at different stages allows the charger to track charging progress and maintain the desired charge profile.  
The result is a controlled and efficient charging process with reduced stress on the battery pack.

---

## Repository Contents

This repository includes the following design artifacts:

- Block diagram.
- Schematic files.
- PCB layout files.
- 3D STEP files.
- BOM.
- Manufacturing outputs.
- Simulation files.
- Measurement results.
- Thermal images.
- Waveform captures.

These files provide a full record of the design process from concept to validation.

---

## Schematic and Simulation

This section can explain how the simulated waveforms were used to verify resonant tank behavior, switching timing, output ripple, and rectifier performance before hardware fabrication.
<img width="1911" height="979" alt="screenshot" src="https://github.com/user-attachments/assets/43e456e0-aff1-47d0-a062-24725d361098" />
<img width="1455" height="807" alt="screenshot 2" src="https://github.com/user-attachments/assets/d13b5095-8a50-40c9-a1dc-ddd3993b9816" />

Input - CM filter - bridge rectifier - boost PFC Schematic
<img width="853" height="444" alt="image" src="https://github.com/user-attachments/assets/3768928a-78ef-458e-98e5-13d22484c92a" />

LLC converter - SR rectifier Schematic
<img width="807" height="497" alt="image" src="https://github.com/user-attachments/assets/0643c8d4-c518-4814-a7f3-5ed1d5aea02b" />

Relay control to connect the battery to the charging schematic.
<img width="676" height="379" alt="image" src="https://github.com/user-attachments/assets/57793c25-3681-4c85-a1cb-ea4753f73185" />



```md



```



---

## PCB Layout

<img width="1184" height="898" alt="image" src="https://github.com/user-attachments/assets/c2f2dff8-50dc-433c-8118-ca4cfe7cd2cf" />


```md



```

The PCB layout maintains 3 mm clearance between neutral and live conductors on the primary side, and 6 mm clearance between primary and secondary domains to support the required isolation barrier and reduce risk of electrical breakdown.
The PCB layout was developed with a strong focus on power integrity, EMI control, and safety isolation. High-frequency switching loops were kept as compact as possible, while sensitive measurement, control, and communication traces were routed away from noisy power nodes. The primary and secondary sections were physically separated to support the isolation barrier, with creepage and clearance considered throughout the board layout and transformer interface. Thermal performance was addressed by spreading losses across the board, using copper for heat dissipation, and positioning major power devices to simplify cooling and reduce local hot spots
---

## 3D and Mechanical Design


<img width="1359" height="648" alt="image" src="https://github.com/user-attachments/assets/5e2e2748-df9c-4726-a15b-ff69fd012288" />

```md


```

---

## Thermal Results
Thermal measurements were taken to identify hotspots across the primary switches, transformer, synchronous rectifier, and auxiliary power components during load testing. The results provide direct feedback on loss distribution and help verify that the layout and cooling strategy are suitable for continuous operation, while also pointing to opportunities for optimization in the next hardware revision.
Vout 24V Iout 5A, 25C ambient

<img width="440" height="333" alt="image" src="https://github.com/user-attachments/assets/42ee4961-4bf2-47f1-92dd-9c7239dc289f" />

```md


```



---

## Prototype

<img width="1920" height="1213" alt="image" src="https://github.com/user-attachments/assets/c77ec121-5f71-4895-ad12-dc00b56e70f9" />

```md




```

Current and voltage were measured at multiple stages of the converter, including the AC input, rectified DC bus, primary switching stage, secondary output, and battery connection point. This allowed the design to be verified stage by stage, from input power quality and bus stability to transformer transfer behavior, rectifier performance, output regulation, and battery charging response.

During constant-current charging, the charger maintains a near-constant output current while the battery voltage rises gradually. As the battery approaches its target voltage, the system transitions into constant-voltage mode, where the voltage is held steady and the current naturally tapers down until the battery is nearly full.

---

## Test Automation

Python was used to automate test capture, organize measurement data, and assist with result analysis.  
This helped reduce manual effort during iterative validation and made it easier to compare test runs across multiple operating points.  
The combination of Python and bench instrumentation improved repeatability and allowed faster debugging during bring-up.

Example test activities:
- Capture voltage and current waveforms.
- Log thermal data.
- Compare simulated and measured results.
- Generate plots for design review.

---

## Future Improvements

Planned enhancements for the next revision include:

- Replacing primary MOSFETs with GaN devices.
- Further optimizing efficiency at light load.
- Improving thermal spreading and airflow paths.
- Expanding BMS communication features.
- Refining EMI performance and layout optimization.
- Adding more diagnostic and telemetry functions in firmware.

---

## Software Tools

The following tools were used in the design process:

- Altium Designer for schematic and PCB design.
- LTspice for circuit simulation.
- STM IDE for embedded firmware development.
- Python for test automation and data analysis.

---

## Summary

This 360W e-bike charger project demonstrates a full hardware development flow from specification to validated prototype.  
It combines high-efficiency isolated power conversion, battery-aware CCCV control, embedded supervision, and structured validation.  
The repository is organized to show both the final implementation and the engineering reasoning behind each design stage.

---
