# Royal Enfield Hunter 350 — Complete Diagnostic & Service Manual

> **Document Revision**: 4.2 | **Effective Date**: January 2025
> **Applicable Model**: Hunter 350 (J1C1 platform, MY 2022–2025)

---

## Table of Contents

1. Introduction & Scope
2. Safety Precautions
3. Technical Specifications
4. Engine System
5. Fuel System & EFI
6. Ignition System
7. Exhaust & Emissions
8. Transmission & Clutch
9. Final Drive & Chain
10. Electrical System
11. Starting System
12. Cooling System
13. Lubrication System
14. Suspension & Steering
15. Braking System
16. Wheels & Tyres
17. Body, Frame & Chassis
18. Instrument Cluster & Electronics
19. Diagnostic Trouble Codes (DTC)
20. Troubleshooting Guide
21. Maintenance Schedule
22. Special Service Tools
23. Parts Catalog (Selection)
24. Warranty & Service Bulletins
25. Emissions Compliance
26. Wiring Diagrams (Reference)
27. Glossary
28. Index

---

## 1. Introduction & Scope

The Royal Enfield Hunter 350 is a modern-classic motorcycle built on the J-platform. It features a 349 cc single-cylinder, air-cooled, fuel-injected engine mated to a 5-speed constant-mesh gearbox. This manual provides complete diagnostic procedures, repair instructions, torque specifications, and troubleshooting guidance.

### 1.1 Intended Audience

- Authorized Royal Enfield Service Centre technicians
- Independent motorcycle workshop mechanics
- Experienced owners performing advanced DIY maintenance

### 1.2 Manual Conventions

| Symbol | Meaning |
|--------|---------|
| ⚠️ WARNING | Risk of personal injury if procedure is not followed |
| 🔧 NOTE | Important technical detail |
| ✅ TIP | Best-practice recommendation |

### 1.3 Model Identification

| Item | Detail |
|------|--------|
| Model Code | J1C1 |
| VIN Location | Right side of steering head |
| Engine Number Location | Left side of crankcase, below cylinder |
| Year of Manufacture | Stamped on VIN plate (10th character) |

---

## 2. Safety Precautions

### 2.1 General Safety

| # | Precaution |
|---|-----------|
| 1 | Always disconnect the battery negative terminal before electrical work. |
| 2 | Use a suitable stand or lift; never work under an unsupported motorcycle. |
| 3 | Wear safety glasses, nitrile gloves, and steel-toe boots. |
| 4 | Allow the engine to cool completely before servicing exhaust or engine components. |
| 5 | Follow lock-out/tag-out (LOTO) procedures for the ignition system. |
| 6 | Keep a Class B fire extinguisher within arm's reach when handling fuel. |
| 7 | Dispose of fluids (oil, coolant, brake fluid) per local environmental regulations. |
| 8 | Do not smoke or use open flames near the fuel system. |

### 2.2 Electrical Safety

- Maximum system voltage: 14.5 V (charging).
- Use insulated tools rated for 50 V minimum.
- When testing high-tension ignition leads, maintain a minimum 25 mm clearance from skin.

### 2.3 Chemical Safety

| Chemical | Hazard | PPE Required |
|----------|--------|-------------|
| Engine Oil (10W-40) | Skin irritant | Nitrile gloves |
| Brake Fluid (DOT 4) | Corrosive to paint | Goggles + gloves |
| Carb Cleaner | Flammable, vapour hazard | Respirator + gloves |
| Anti-Seize Compound | Skin sensitiser | Gloves |
| Chain Lubricant | Flammable | Ventilated area |

---

## 3. Technical Specifications

### 3.1 Engine Specifications

| Parameter | Value |
|-----------|-------|
| Engine Type | Single-cylinder, 4-stroke, air-cooled, SOHC |
| Displacement | 349.34 cc |
| Bore × Stroke | 72 mm × 85.8 mm |
| Compression Ratio | 9.5 : 1 |
| Maximum Power | 20.2 PS (14.9 kW) @ 6,500 rpm |
| Maximum Torque | 27 Nm (19.9 lb-ft) @ 4,000 rpm |
| Valve Configuration | 2 valves (1 intake, 1 exhaust) |
| Intake Valve Clearance (cold) | 0.10 mm (±0.02 mm) |
| Exhaust Valve Clearance (cold) | 0.15 mm (±0.02 mm) |
| Idle Speed | 1,250 ± 100 rpm |
| Engine Oil Capacity | 1.7 L (with filter change) |
| Oil Grade | 10W-40, API SL / JASO MA2 |

### 3.2 Chassis & Dimensions

| Parameter | Value |
|-----------|-------|
| Frame Type | Half-duplex split cradle, steel |
| Wheelbase | 1,370 mm |
| Seat Height | 790 mm |
| Ground Clearance | 150 mm |
| Kerb Weight | 181 kg |
| Fuel Tank Capacity | 13 L (reserve: 2.5 L) |
| Front Suspension | 41 mm telescopic fork, 130 mm travel |
| Rear Suspension | Twin shock absorbers, 6-step preload, 102 mm travel |
| Front Brake | 300 mm disc, twin-piston floating caliper |
| Rear Brake | 270 mm disc, single-piston floating caliper |
| Front Tyre | 100/80-17 M/C 52P, tubeless |
| Rear Tyre | 130/70-17 M/C 62P, tubeless |

### 3.3 Electrical Specifications

| Parameter | Value |
|-----------|-------|
| Battery | 12 V, 9 Ah, MF (maintenance-free) |
| Alternator Output | 15 A @ 5,000 rpm |
| Headlamp | LED, 40 W |
| Tail/Brake Lamp | LED |
| Spark Plug | NGK MR8C-9N (or equivalent) |
| Spark Plug Gap | 0.8–0.9 mm |
| Fuse Box | Blade type, main 30 A, auxiliaries 10/15 A |

### 3.4 Transmission Specifications

| Parameter | Value |
|-----------|-------|
| Type | 5-speed, constant mesh |
| Clutch | Wet, multi-plate, cable-operated |
| Primary Reduction | 3.042 (73/24) |
| Final Reduction | 2.800 (42/15) |
| Gear Ratios | 1st: 2.846 / 2nd: 1.812 / 3rd: 1.318 / 4th: 1.040 / 5th: 0.878 |
| Drive Chain | 520, O-ring, 106 links |
| Chain Slack | 20–30 mm (measured at mid-point of lower run) |

---

## 4. Engine System

### 4.1 Engine Overview

The Hunter 350 engine is a long-stroke, counter-balanced single producing smooth power delivery. Key design features:

- **Balancer shaft**: Gear-driven, reduces primary vibration by approximately 70%.
- **Forged crankshaft**: Nitrided journals for extended life.
- **Aluminium alloy cylinder head**: Hemispherical combustion chamber.
- **Cast-iron cylinder liner**: Plateau-honed for optimal ring seating.
- **SOHC valve train**: Chain-driven camshaft with rocker arms.

### 4.2 Cylinder Head Removal

**Tools Required**: 8 mm, 10 mm, 12 mm sockets; torque wrench (10–60 Nm); valve spring compressor.

1. Remove the fuel tank and seat.
2. Disconnect the intake manifold and throttle body assembly.
3. Remove the exhaust header pipe (2 × M8 × 35 mm studs, 25 Nm).
4. Remove the cam chain tensioner.
5. Remove the cam cover (4 × M6 bolts, 10 Nm).
6. Mark the cam chain and sprocket timing position with a paint pen.
7. Remove the camshaft bearing caps (note directional arrows).
8. Remove the cylinder head bolts in reverse sequence (5–4–3–2–1 pattern).
9. Lift the head off carefully; do not damage the gasket surface.

**Torque Specifications — Cylinder Head Re-assembly**:

| Step | Fastener | Torque |
|------|----------|--------|
| 1 | Cylinder head bolts (M10) — initial pass | 15 Nm |
| 2 | Cylinder head bolts (M10) — 90° angle tightening | +90° |
| 3 | Camshaft bearing caps (M8) | 12 Nm |
| 4 | Cam cover (M6) | 10 Nm |
| 5 | Exhaust header studs (M8) | 25 Nm |

### 4.3 Piston & Ring Inspection

| Measurement | Standard | Service Limit |
|-------------|----------|---------------|
| Piston diameter (at skirt, perpendicular to pin) | 71.96–71.98 mm | 71.90 mm |
| Piston-to-cylinder clearance | 0.02–0.04 mm | 0.10 mm |
| Top ring end gap | 0.15–0.30 mm | 0.50 mm |
| Second ring end gap | 0.30–0.50 mm | 0.70 mm |
| Oil ring end gap | 0.20–0.70 mm | 0.90 mm |
| Piston pin bore | 18.002–18.008 mm | 18.03 mm |
| Piston pin OD | 17.996–18.000 mm | 17.98 mm |

### 4.4 Valve Train Service

**Valve Clearance Adjustment**:

1. Remove the tappet covers (2 × M6, 10 Nm).
2. Rotate the engine to TDC on compression stroke (both valves closed, timing mark aligned).
3. Insert a feeler gauge between the rocker arm and valve stem.
4. Intake: 0.10 mm (±0.02 mm). Exhaust: 0.15 mm (±0.02 mm).
5. If out of specification, loosen the locknut (10 mm) and turn the adjusting screw.
6. Retighten the locknut to 16 Nm while holding the adjusting screw.
7. Re-check the clearance after tightening.

**Cam Chain Tensioner**:

- Type: Automatic, hydraulic, ratchet-style.
- Inspection: Push the tensioner plunger by hand; it should not move more than 2 mm.
- Replacement interval: Every 40,000 km or if rattling noise is detected at idle.

### 4.5 Compression Test

1. Warm the engine to operating temperature (oil temp ≥ 70 °C).
2. Remove the spark plug.
3. Install the compression gauge adapter.
4. Hold the throttle wide open and crank the engine 5–6 revolutions.
5. Record the reading.

| Condition | Specification |
|-----------|---------------|
| Standard compression | 1,100–1,300 kPa (160–190 psi) |
| Minimum compression | 900 kPa (130 psi) |
| Maximum cylinder variation | N/A (single cylinder) |

If compression is low, perform a wet test (add 5 ml oil through spark plug hole) to differentiate ring wear from valve leakage.

---

## 5. Fuel System & EFI

### 5.1 System Overview

The Hunter 350 uses a port-injected EFI system with the following components:

- **ECU** (Bosch EMS 2.5): Controls fuel injection timing, quantity, and ignition advance.
- **Throttle Body**: 38 mm bore, single butterfly valve.
- **Fuel Injector**: 4-hole, 165 cc/min @ 3 bar.
- **Fuel Pump**: In-tank, electric, 3.5 bar operating pressure.
- **Sensors**: TPS, MAP, IAT, ECT, O₂ (lambda), CKP, CMP.

### 5.2 Throttle Body Service

1. Remove the air filter box (2 × M6 bolts + 2 rubber mounts).
2. Disconnect the TPS, ISC (idle speed control) motor, and MAP sensor connectors.
3. Remove the throttle body from the intake manifold (2 × M6 × 25 mm, 10 Nm).
4. Clean the throttle plate and bore with carburettor cleaner.
5. Inspect the throttle plate for scoring or wear.
6. Check the ISC motor: apply 12 V and verify plunger extends/retracts smoothly.
7. Reinstall with a new gasket; torque to 10 Nm.

⚠️ **WARNING**: Do not use abrasive materials on the throttle bore. The DLC (Diamond-Like Carbon) coating will be damaged.

### 5.3 Fuel Injector Testing

| Test | Specification |
|------|---------------|
| Resistance | 12.0 ± 0.6 Ω @ 20 °C |
| Spray Pattern | Cone, 15° angle |
| Leak Test | No drip for 60 seconds @ 3.5 bar |
| Flow Rate | 165 ± 5 cc/min @ 3 bar |

### 5.4 Fuel Pump Specifications

| Parameter | Value |
|-----------|-------|
| Type | Brushless DC, in-tank |
| Operating Pressure | 3.0–3.5 bar |
| Flow Rate | ≥ 30 L/hr |
| Operating Voltage | 9–16 V DC |
| Current Draw | ≤ 3.5 A |

**Fuel Pump Test Procedure**:
1. Remove the fuel tank and access the pump module.
2. Connect a fuel pressure gauge to the delivery line.
3. Apply 12 V to the pump connector.
4. Pressure should reach 3.0 bar within 3 seconds.
5. Shut off power; pressure should hold for 60 seconds (no drop > 0.5 bar).

### 5.5 Sensor Reference Values

| Sensor | Condition | Expected Value |
|--------|-----------|---------------|
| TPS | Throttle closed | 0.45–0.55 V |
| TPS | Throttle fully open | 4.0–4.5 V |
| MAP | Ignition ON, engine off | 95–105 kPa |
| MAP | Idle | 25–35 kPa |
| IAT | Ambient 25 °C | 2.0–2.5 V |
| ECT | Engine cold (25 °C) | 2.5–3.0 kΩ |
| ECT | Engine hot (90 °C) | 250–350 Ω |
| O₂ Sensor | Lean | < 0.2 V |
| O₂ Sensor | Rich | > 0.7 V |
| CKP | Cranking | AC signal, 0.5–2.0 V peak |
| CMP | Running | Square wave, 0–5 V |

---

## 6. Ignition System

### 6.1 System Description

The ignition system is a full-transistor type controlled by the ECU. The CKP (Crankshaft Position) sensor provides the trigger signal. The ECU calculates ignition advance based on RPM, load, temperature, and knock sensor input (where fitted).

### 6.2 Ignition Timing

| Condition | Timing |
|-----------|--------|
| Initial (at idle) | 12° BTDC ± 2° |
| Maximum advance | 32° BTDC @ 4,500 rpm |

**Checking Procedure**:
1. Connect a timing light to the spark plug lead.
2. Start the engine and warm to operating temperature.
3. Point the timing light at the timing marks on the flywheel/stator cover.
4. At idle (1,250 rpm), the mark should align with the 12° indicator.
5. If adjustment is needed, the ECU must be reflashed (no manual adjustment).

### 6.3 Ignition Coil Testing

| Test | Specification |
|------|---------------|
| Primary Resistance | 0.5–0.7 Ω |
| Secondary Resistance | 6.5–8.5 kΩ |
| Insulation Resistance | > 10 MΩ (at 500 V megger) |

### 6.4 Spark Plug Service

1. Remove the spark plug cap (pull straight; do not twist).
2. Use a 16 mm thin-wall spark plug socket.
3. Inspect the electrode condition:

| Condition | Diagnosis |
|-----------|-----------|
| Light tan/grey deposits | Normal combustion |
| Wet, black, oily | Oil burning — check rings/valve seals |
| Dry, black, sooty | Rich mixture — check injector/sensors |
| White, blistered | Lean mixture / overheating |
| Eroded electrodes | Excessive mileage — replace |

4. Gap new plug to 0.8–0.9 mm.
5. Apply a thin coat of anti-seize to threads.
6. Install hand-tight, then torque to 12 Nm.

---

## 7. Exhaust & Emissions

### 7.1 Exhaust System Components

The exhaust consists of:
- **Header pipe**: Stainless steel, connects to the cylinder head (2 × M8 studs).
- **Catalytic converter**: Three-way (TWC), integral to the header mid-section.
- **Muffler**: Stainless steel shell, internal baffle design.
- **Lambda (O₂) sensor**: Heated, narrow-band, threaded into the header pipe.

### 7.2 Catalytic Converter

| Parameter | Specification |
|-----------|---------------|
| Type | Three-Way Catalyst (TWC) |
| Light-off Temperature | 250–300 °C |
| Operating Temperature | 350–800 °C |
| Precious Metal Loading | Pt/Pd/Rh |
| Expected Life | 80,000 km (under normal conditions) |

⚠️ **WARNING**: The catalytic converter can reach 800 °C. Never touch or place flammable materials near it after engine operation.

### 7.3 Emission Standards (BS-VI)

| Parameter | Limit |
|-----------|-------|
| CO | ≤ 1.0 g/km |
| HC | ≤ 0.10 g/km |
| NOx | ≤ 0.06 g/km |
| Evaporative Emissions | ≤ 2.0 g/test |

### 7.4 Emission Test Procedure

1. Warm the engine to operating temperature (coolant ≥ 80 °C).
2. Connect the exhaust gas analyser probe to the tailpipe.
3. Record readings at idle (1,250 rpm) and elevated idle (3,000 rpm).
4. Compare against the BS-VI limits above.
5. If CO is high: check O₂ sensor, fuel pressure, injector spray pattern.
6. If HC is high: check ignition system, valve clearances, compression.

---

## 8. Transmission & Clutch

### 8.1 Clutch System

The wet, multi-plate clutch uses 6 friction plates and 5 steel plates, operated by a cable mechanism.

| Parameter | Specification |
|-----------|---------------|
| Friction Plate Thickness (new) | 3.00 mm |
| Friction Plate Thickness (service limit) | 2.60 mm |
| Steel Plate Warpage Limit | 0.10 mm |
| Clutch Spring Free Length (new) | 37.5 mm |
| Clutch Spring Free Length (service limit) | 35.5 mm |
| Cable Free Play (at lever) | 10–15 mm |

### 8.2 Clutch Adjustment

1. Loosen the cable adjuster lock nut at the lever.
2. Turn the adjuster to achieve 10–15 mm free play.
3. Lock the adjuster nut.
4. Check at the engine-side adjuster (bottom of clutch cover) if full range is insufficient at the lever end.
5. Test: with engine idling and clutch lever pulled, shift into 1st gear — the motorcycle should not creep.

### 8.3 Gear Shift Mechanism

- **Shift Drum**: Grooved drum controlling fork positions.
- **Shift Forks**: 3 forks, made from hardened steel.
- **Detent Mechanism**: Spring-loaded roller on the shift drum.

**Common Issues**:
- Hard shifting cold: Normal for first 2 minutes; allow oil to warm.
- False neutral between 2nd and 3rd: Check shift fork bending (max 0.3 mm).
- Popping out of gear: Worn shift drum grooves or dog engagement — requires transmission overhaul.

---

## 9. Final Drive & Chain

### 9.1 Drive Chain Specifications

| Parameter | Value |
|-----------|-------|
| Chain Type | 520, O-ring sealed |
| Number of Links | 106 |
| Front Sprocket | 15 teeth |
| Rear Sprocket | 42 teeth |
| Chain Slack (mid-lower run) | 20–30 mm |

### 9.2 Chain Maintenance

**Every 1,000 km or after riding in rain/dust**:
1. Place motorcycle on centre stand (or paddock stand).
2. Clean chain with kerosene and a soft brush; do NOT use a pressure washer.
3. Dry the chain completely.
4. Apply O-ring compatible chain lubricant to the inside of the lower run while slowly rotating the rear wheel.
5. Wipe excess lubricant.

**Chain Tension Adjustment**:
1. Loosen the rear axle nut (24 mm, torque: 80 Nm).
2. Turn the chain adjuster bolts equally on both sides.
3. Measure slack at the tightest point of the chain (rotate wheel to find it).
4. Adjust to 20–30 mm.
5. Verify rear wheel alignment using the swingarm index marks.
6. Retighten the rear axle nut to 80 Nm.

### 9.3 Chain & Sprocket Replacement

Replace the chain, front sprocket, and rear sprocket as a set when:
- Chain stretch exceeds 2% (measure 20 pitches: standard 317.5 mm, replace at 323.9 mm).
- Sprocket teeth show hooking, sharpening, or missing tips.
- O-ring seals are visibly damaged (chain section feels stiff or binds).

---

## 10. Electrical System

### 10.1 Charging System

| Component | Specification |
|-----------|---------------|
| Alternator Type | 3-phase, permanent magnet |
| Output | 15 A @ 5,000 rpm |
| Regulator/Rectifier | Full-wave, MOSFET type |
| Charging Voltage | 13.5–14.5 V @ 5,000 rpm |

**Alternator Output Test**:
1. Start the engine and warm to operating temperature.
2. Set multimeter to AC volts.
3. Measure across any two of the three stator output wires (disconnected from R/R).
4. At 5,000 rpm, each pair should read 50–80 VAC.
5. If any pair reads significantly lower, the stator is likely faulty.

**Regulator/Rectifier Test**:
1. With the engine running at 5,000 rpm, measure DC voltage across the battery terminals.
2. Should read 13.5–14.5 V.
3. If voltage exceeds 15.0 V: R/R is failing (overcharging) — replace immediately.
4. If voltage is below 13.0 V: check stator output first, then R/R.

### 10.2 Battery

| Parameter | Specification |
|-----------|---------------|
| Type | 12 V, 9 Ah, VRLA (maintenance-free) |
| Cold Cranking Amps | ≥ 120 CCA |
| Fully Charged Voltage | 12.7–13.0 V |
| Low Charge Threshold | < 12.4 V |
| Charging Current (external charger) | 0.9 A (trickle) |

### 10.3 Fuse Locations

| Fuse | Rating | Circuit |
|------|--------|---------|
| Main | 30 A | All circuits |
| ECU | 10 A | Engine management |
| Headlamp | 15 A | LED headlamp |
| Fuel Pump | 10 A | Fuel pump relay |
| Accessories | 10 A | Horn, indicators, brake lamp |
| Ignition | 10 A | Ignition coil, injector |

---

## 11. Starting System

### 11.1 Starter Motor

| Parameter | Specification |
|-----------|---------------|
| Type | Planetary gear reduction |
| Rated Voltage | 12 V |
| No-Load Current | ≤ 50 A |
| Stall Current | ≤ 350 A |
| Brush Length (new) | 12.0 mm |
| Brush Length (service limit) | 6.5 mm |

### 11.2 Starting Circuit Diagnosis

**Engine does not crank**:
1. Check battery voltage: ≥ 12.4 V?
2. Check the kill switch and side-stand switch.
3. Check the clutch interlock switch (must be pulled in for starting on some variants).
4. Check the starter relay: apply 12 V to the relay coil — you should hear a click and continuity across the main contacts.
5. Check the starter motor: apply 12 V directly — it should spin freely.
6. If motor spins but engine doesn't crank: check the starter clutch (one-way sprag clutch).

---

## 12. Cooling System

### 12.1 Air-Cooling Design

The Hunter 350 is air-cooled. The cylinder and head have cooling fins that dissipate heat. No liquid coolant or radiator is used.

**Maintenance**:
- Keep cooling fins free of mud, oil, and debris.
- Inspect fins for damage (broken fins reduce cooling efficiency by up to 5% per fin).
- In stop-and-go traffic above 40 °C ambient, avoid sustained idling beyond 10 minutes.

### 12.2 Engine Temperature Monitoring

The ECT (Engine Coolant Temperature — misnomer, actually measures cylinder head temperature) sensor feeds the ECU. If temperature exceeds the threshold:

| Level | Temperature | Action |
|-------|-------------|--------|
| Normal | 80–110 °C | No action |
| Warning | 110–125 °C | ECU retards timing, MIL flashes |
| Critical | > 125 °C | ECU reduces fuel cut / limp mode |

---

## 13. Lubrication System

### 13.1 Oil Circuit

The wet-sump lubrication system uses a trochoid (gerotor) oil pump mounted on the crankshaft:

1. Oil is drawn from the sump through a mesh screen.
2. The pump pressurises oil to 3.5–4.5 bar @ 4,000 rpm.
3. Oil passes through a cartridge filter.
4. Pressurised oil feeds the crankshaft main bearings, con-rod bearing, camshaft journals, rocker arms, and cylinder wall.
5. Oil returns to the sump by gravity.

### 13.2 Oil Change Procedure

**Interval**: Every 5,000 km or 6 months (whichever comes first). First service at 500 km.

1. Warm the engine for 5 minutes (improves drainage).
2. Place a drain pan under the engine.
3. Remove the drain bolt (M14 × 1.5, 17 mm wrench). Torque on reinstall: 25 Nm.
4. Remove the oil filter cover (3 × M6 bolts, 10 Nm) on the right side of the engine.
5. Remove the used filter cartridge.
6. Install a new OEM filter (or equivalent meeting JASO MA2 filtration spec).
7. Reinstall the filter cover with a new O-ring.
8. Reinstall the drain bolt with a new crush washer (M14 aluminium).
9. Fill with 1.7 L of 10W-40, API SL / JASO MA2 oil.
10. Start the engine, let idle for 2 minutes, shut off.
11. Wait 3 minutes, then check oil level on the dipstick — should be between the two marks.

### 13.3 Oil Pressure Specification

| Condition | Minimum Pressure |
|-----------|-----------------|
| Idle (1,250 rpm), hot | 0.8 bar |
| 4,000 rpm, hot | 3.5 bar |

If oil pressure is low, check:
- Oil level and condition.
- Oil pump wear (gerotor clearances).
- Main bearing clearances.
- Oil pressure relief valve (stuck open).

---

## 14. Suspension & Steering

### 14.1 Front Fork Service

**Fork Oil Change** (every 20,000 km):

1. Remove the front wheel, fender, and brake caliper (do not disconnect brake hose — hang caliper with wire).
2. Loosen the upper and lower triple clamp pinch bolts.
3. Slide out the fork legs.
4. Remove the fork cap (requires a 32 mm socket or fork cap wrench).
5. Drain old oil by pumping the fork tube.
6. Measure and pour new fork oil: 265 ml per leg, SAE 10 weight.
7. Pump the fork tube 10 times to bleed air.
8. Set oil level: 130 mm from top of inner tube (with spring removed, fully compressed).
9. Reinstall the fork cap and assemble in reverse.

| Fork Specification | Value |
|-------------------|-------|
| Inner Tube Diameter | 41 mm |
| Travel | 130 mm |
| Fork Oil | SAE 10 (10W), 265 ml/leg |
| Oil Level | 130 mm from top (spring removed, compressed) |
| Spring Rate | 0.65 kg/mm |
| Standard Preload | Spacer length: 20 mm |

### 14.2 Rear Shock Absorbers

| Specification | Value |
|---------------|-------|
| Type | Twin, coil-over, 6-step preload adjustable |
| Travel | 102 mm |
| Spring Rate | 85 N/mm |
| Damping | Non-adjustable |
| Eye-to-Eye Length | 320 mm |

**Inspection**:
- Check for oil leaks around the shaft seal.
- Compress and release — rebound should be smooth with no topping-out or bottoming-out clunk.
- Replace if the shock body is dented, bent, or leaking.

### 14.3 Steering Head Bearings

| Parameter | Specification |
|-----------|---------------|
| Type | Tapered roller bearings (upper and lower) |
| Preload | Slight resistance when turning; no play when rocking forks front-to-back |
| Replacement Interval | As needed; inspect every 20,000 km |

---

## 15. Braking System

### 15.1 Brake Specifications

| Parameter | Front | Rear |
|-----------|-------|------|
| Disc Diameter | 300 mm | 270 mm |
| Disc Thickness (new) | 5.0 mm | 5.0 mm |
| Disc Thickness (minimum) | 4.0 mm | 4.0 mm |
| Disc Runout Limit | 0.15 mm | 0.15 mm |
| Pad Thickness (new) | 4.5 mm | 4.5 mm |
| Pad Thickness (minimum) | 1.0 mm | 1.0 mm |
| Caliper Piston Diameter | 30.2 mm (×2) | 34 mm (×1) |
| Brake Fluid | DOT 4 | DOT 4 |

### 15.2 Brake Pad Replacement

1. Remove the caliper mounting bolts (2 × M8, 30 Nm).
2. Slide the caliper off the disc.
3. Push the pistons back using a brake piston tool (or large flat screwdriver — carefully).
4. Remove old pads and anti-squeal shims.
5. Install new pads with shims and any retaining clips.
6. Reinstall the caliper; torque bolts to 30 Nm.
7. Pump the brake lever until firm pressure is felt.

### 15.3 Brake Fluid Replacement

**Interval**: Every 2 years regardless of mileage (hygroscopic degradation).

1. Remove the master cylinder cap and diaphragm.
2. Attach a bleed tube to the caliper bleed nipple; submerge the other end in a container with clean fluid.
3. Open the bleed nipple 1/4 turn.
4. Slowly squeeze and release the brake lever, keeping the reservoir topped up.
5. Continue until clear, bubble-free fluid flows from the bleed tube.
6. Close the bleed nipple and torque to 7 Nm.
7. Top up the reservoir to the MAX line.

---

## 16. Wheels & Tyres

### 16.1 Wheel Specifications

| Parameter | Front | Rear |
|-----------|-------|------|
| Rim Size | 17 × 2.75 | 17 × 3.50 |
| Type | Cast aluminium alloy, tubeless |
| Axle Diameter | 17 mm | 17 mm |
| Axle Nut Torque | 65 Nm | 80 Nm |

### 16.2 Tyre Pressures

| Condition | Front | Rear |
|-----------|-------|------|
| Solo rider | 28 psi (193 kPa) | 32 psi (220 kPa) |
| Rider + pillion | 28 psi | 36 psi (248 kPa) |

### 16.3 Wheel Bearing Inspection

1. Lift the wheel off the ground.
2. Spin the wheel — it should rotate freely without noise.
3. Grab the wheel at top and bottom; rock it — there should be no play.
4. If play or roughness is detected, replace the wheel bearings.
5. Bearing type: 6204-2RS (front and rear, both sides).

---

## 17. Body, Frame & Chassis

### 17.1 Frame Inspection

- Visually inspect all welds for cracks, especially at the steering head, swingarm pivot, and engine mounting points.
- Check frame alignment: use a straight-edge along the frame rails; maximum deviation 2 mm.
- Check swingarm pivot bolt torque: 55 Nm.
- Check engine mounting bolt torques (refer to engine section).

### 17.2 Fastener Torque Reference

| Location | Fastener | Torque |
|----------|----------|--------|
| Steering head nut (top) | M24 × 1.0 | 25 Nm |
| Triple clamp upper pinch | M8 | 23 Nm |
| Triple clamp lower pinch | M8 | 23 Nm |
| Handlebar clamp | M8 | 25 Nm |
| Footpeg bracket | M10 | 40 Nm |
| Side stand bolt | M10 | 30 Nm |
| Side stand spring | — | Inspect annually |
| Rear grab rail | M8 | 25 Nm |

---

## 18. Instrument Cluster & Electronics

### 18.1 Instrument Cluster

The LCD cluster displays:
- Speedometer (digital)
- Tachometer (bar graph)
- Odometer / Trip meters (A and B)
- Fuel level gauge
- Gear position indicator
- Clock
- MIL (Malfunction Indicator Lamp)
- ABS indicator (where fitted)
- Turn signal indicators
- High-beam indicator
- Neutral indicator

### 18.2 Tripper Navigation (where fitted)

The Royal Enfield Tripper turn-by-turn navigation pod uses Bluetooth to connect to the rider's smartphone via the Royal Enfield app.

**Troubleshooting**:
- Tripper not connecting: Ensure Bluetooth is enabled; unpair and re-pair the device.
- Incorrect direction display: Update the Royal Enfield app to the latest version.
- Display blank: Check the Tripper fuse (5 A) and connector behind the headlamp.

---

## 19. Diagnostic Trouble Codes (DTC)

### 19.1 Reading DTCs

1. Turn the ignition ON (do not start the engine).
2. Observe the MIL (check engine light):
   - Steady ON for 3 seconds then OFF = no stored faults.
   - Flashing = active fault(s) stored.
3. Use an OBD-II compatible scan tool (or the Royal Enfield diagnostic tool) connected to the 16-pin diagnostic connector under the seat.
4. Read and record all DTCs.

### 19.2 DTC Table

| DTC Code | Description | Possible Cause | Diagnostic Steps |
|----------|-------------|----------------|------------------|
| P0107 | MAP Sensor Circuit Low | Broken wire, faulty sensor | Check wiring, measure sensor output voltage; replace if < 0.2 V at key-on |
| P0108 | MAP Sensor Circuit High | Short to battery, sensor failure | Check for short in harness; replace sensor if reading > 4.8 V |
| P0112 | IAT Sensor Circuit Low | Short to ground | Measure resistance; should be 2–3 kΩ at 25 °C |
| P0113 | IAT Sensor Circuit High | Open circuit | Check connector, wiring continuity |
| P0117 | ECT Sensor Circuit Low | Short to ground | Measure resistance at connector; 2.5 kΩ at 25 °C |
| P0118 | ECT Sensor Circuit High | Open circuit | Check wiring and connector |
| P0122 | TPS Circuit Low | TPS failure, wiring fault | Verify TPS voltage: 0.45–0.55 V at closed throttle |
| P0123 | TPS Circuit High | Short to 5 V supply | Check for pinched wires; replace TPS if shorted |
| P0130 | O₂ Sensor Circuit (Bank 1) | Sensor degraded | Check sensor voltage swing (0.1–0.9 V); replace if sluggish |
| P0131 | O₂ Sensor Low Voltage | Lean exhaust, air leak | Check for intake/exhaust leaks; check fuel pressure |
| P0132 | O₂ Sensor High Voltage | Rich exhaust | Check injector flow, fuel pressure regulator |
| P0201 | Injector Circuit Open | Wiring break, connector issue | Measure injector resistance: 12 ± 0.6 Ω |
| P0261 | Injector Circuit Low | Short to ground | Inspect harness for chafing |
| P0262 | Injector Circuit High | Short to battery | Check harness routing near battery cables |
| P0335 | CKP Sensor Circuit | Sensor failure, air gap | Check sensor air gap: 0.5–1.0 mm; replace if no signal |
| P0336 | CKP Sensor Range/Performance | Reluctor ring damage | Inspect the flywheel reluctor teeth for damage |
| P0340 | CMP Sensor Circuit | Sensor failure | Check connector; measure signal with oscilloscope |
| P0505 | Idle Speed Control System | ISC motor fault | Test motor with 12 V; plunger should extend |
| P0560 | System Voltage Low | Battery weak, charging fault | Check battery voltage and alternator output |
| P0562 | System Voltage Low (critical) | Alternator failure | Test stator output, R/R; replace as needed |
| P0650 | MIL Circuit | Bulb/LED failure | Check instrument cluster connector |
| P1601 | ECU Internal Error | ECU hardware fault | Reset ECU; replace if fault persists after re-flash |
| P2101 | Throttle Actuator Control Range | Electronic throttle fault | (Note: Hunter 350 uses cable throttle — DTC rare, check ECU version) |
| P2195 | O₂ Sensor Stuck Lean | Sensor aging, air leak | Replace O₂ sensor; check intake manifold gasket |
| P2196 | O₂ Sensor Stuck Rich | Fuel system issue | Check fuel pressure, injector, purge valve |
| C0035 | ABS Wheel Speed Sensor Front | Sensor gap, damaged tone ring | Check air gap: 0.5–1.5 mm; inspect tone ring for debris |
| C0040 | ABS Wheel Speed Sensor Rear | Sensor failure | Replace sensor; check wiring |
| C0051 | ABS Pump Motor | Pump failure | Check ABS fuse; test pump motor |
| C0070 | ABS ECU Communication | CAN bus error | Check CAN wiring between main ECU and ABS module |

### 19.3 Clearing DTCs

1. Connect the scan tool.
2. Navigate to "Clear Codes" or "Erase DTCs".
3. Confirm the action.
4. Turn the ignition OFF, wait 10 seconds, then turn ON.
5. Verify the MIL is no longer flashing.
6. Test ride the motorcycle for at least 5 km to confirm no DTCs return.

---

## 20. Troubleshooting Guide

### 20.1 Engine Does Not Start

| Check | Action |
|-------|--------|
| Kill switch | Ensure in RUN position |
| Side stand | Retract fully (interlock switch) |
| Clutch lever | Pull in (interlock on some models) |
| Battery voltage | ≥ 12.4 V; charge or replace if low |
| Fuel level | Minimum 1 L; check fuel gauge accuracy |
| Fuel pump prime | Turn ignition ON — listen for 2-second pump prime buzz |
| Spark | Remove plug, ground against engine, crank — look for strong blue spark |
| Compression | Perform compression test (Section 4.5) |
| DTCs | Read codes (Section 19) |

### 20.2 Engine Stalls at Idle

| Possible Cause | Diagnostic Step |
|----------------|-----------------|
| Low idle speed | Check idle RPM (1,250 ± 100); adjust via ISC or ECU reset |
| Vacuum leak | Spray carb cleaner around intake joints — RPM change indicates a leak |
| Dirty throttle body | Clean per Section 5.2 |
| Faulty ISC motor | Test with 12 V (Section 5.2) |
| Clogged air filter | Inspect / replace |
| Old fuel | Drain and refill with fresh fuel |

### 20.3 Poor Fuel Economy

| Possible Cause | Expected Range | Diagnostic Step |
|----------------|----------------|-----------------|
| Under-inflated tyres | 35–40 km/L | Check tyre pressures (Section 16.2) |
| Dirty air filter | — | Inspect / replace |
| Dragging brakes | — | Spin each wheel freely; check pad clearance |
| Chain too tight | — | Check chain slack (Section 9.2) |
| Faulty O₂ sensor | — | Check O₂ response (Section 5.5); replace if sluggish |
| Fuel leak | — | Inspect fuel lines, tank seal, injector O-ring |

### 20.4 Excessive Vibration

| Possible Cause | Diagnostic Step |
|----------------|-----------------|
| Worn engine mounts | Inspect rubber mounts for cracking; replace if hardened |
| Balancer shaft issue | Requires engine teardown; check balancer timing |
| Loose fasteners | Check all frame, engine, and handlebar bolts |
| Wheel imbalance | Re-balance both wheels |
| Worn chain/sprockets | Inspect per Section 9.3 |

### 20.5 ABS Warning Light ON

| Check | Action |
|-------|--------|
| ABS fuse | Check 15 A ABS fuse |
| Wheel speed sensors | Inspect air gap, clean debris from tone rings |
| ABS module connector | Check for corrosion, bent pins |
| DTCs | Read ABS-specific codes (C0035, C0040, C0051, C0070) |
| Battery voltage | Low voltage can cause ABS errors; charge battery |

### 20.6 Clutch Slipping

| Possible Cause | Diagnostic Step |
|----------------|-----------------|
| Cable too tight | Check free play: 10–15 mm at lever |
| Worn friction plates | Measure thickness (min 2.60 mm) |
| Contaminated plates | Oil contamination — replace plates and check for oil leaks |
| Weak springs | Measure free length (min 35.5 mm) |

### 20.7 Overheating (High Temperature Warning)

| Possible Cause | Diagnostic Step |
|----------------|-----------------|
| Cooling fins blocked | Clean fins, remove mud/debris |
| Oil level low | Check and top up |
| Oil grade incorrect | Use 10W-40 JASO MA2; heavier grades impede cooling |
| Prolonged idling in traffic | Avoid idling > 10 min in ambient > 40 °C |
| ECT sensor fault | Read DTC P0117/P0118; check sensor resistance |

---

## 21. Maintenance Schedule

### 21.1 Standard Service Intervals

| Service Item | 500 km | 5,000 km | 10,000 km | 15,000 km | 20,000 km |
|-------------|--------|----------|-----------|-----------|-----------|
| Engine oil & filter | ✅ | ✅ | ✅ | ✅ | ✅ |
| Valve clearance | — | — | ✅ | — | ✅ |
| Air filter — clean | — | ✅ | ✅ | ✅ | ✅ |
| Air filter — replace | — | — | ✅ | — | ✅ |
| Spark plug — inspect | — | ✅ | ✅ | ✅ | ✅ |
| Spark plug — replace | — | — | ✅ | — | ✅ |
| Drive chain — clean & lube | ✅ | ✅ | ✅ | ✅ | ✅ |
| Drive chain — adjust | ✅ | ✅ | ✅ | ✅ | ✅ |
| Brake pads — inspect | — | ✅ | ✅ | ✅ | ✅ |
| Brake fluid — replace | — | — | — | — | ✅ |
| Clutch free play — adjust | ✅ | ✅ | ✅ | ✅ | ✅ |
| Throttle cable — inspect | — | ✅ | ✅ | ✅ | ✅ |
| Coolant fan / fins | — | ✅ | ✅ | ✅ | ✅ |
| Front fork oil | — | — | — | — | ✅ |
| Steering head bearings | — | — | — | — | ✅ |
| Wheel bearings | — | — | — | — | ✅ |
| Battery — check | ✅ | ✅ | ✅ | ✅ | ✅ |
| General fastener check | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## 22. Special Service Tools

| Tool | Part Number | Usage |
|------|-------------|-------|
| Flywheel puller | RE-SST-001 | Remove flywheel/rotor |
| Valve spring compressor | RE-SST-002 | Compress valve springs for removal |
| Fork cap wrench (32 mm) | RE-SST-003 | Remove/install fork caps |
| Clutch hub holder | RE-SST-004 | Hold clutch hub during nut removal |
| Oil filter wrench | RE-SST-005 | Remove spin-on oil filter (if applicable) |
| Cam chain tensioner reset tool | RE-SST-006 | Reset automatic tensioner |
| Diagnostic connector adapter | RE-SST-007 | Connect scan tool to 16-pin port |
| Bearing driver set | RE-SST-008 | Install wheel and steering bearings |

---

## 23. Parts Catalog (Selection)

| Category | Part Description | OEM Part No. | Qty |
|----------|-----------------|--------------|-----|
| Engine | Piston ring set | 570174/A | 1 set |
| Engine | Cylinder head gasket | 570175/B | 1 |
| Engine | Cam chain | 570176/C | 1 |
| Engine | Oil filter cartridge | 888464/A | 1 |
| Fuel | Fuel injector | 591890/A | 1 |
| Fuel | Fuel pump assembly | 591891/B | 1 |
| Fuel | Throttle body assembly | 591892/C | 1 |
| Ignition | Spark plug (NGK MR8C-9N) | 598001/A | 1 |
| Ignition | Ignition coil | 598002/B | 1 |
| Exhaust | Catalytic converter | 585010/A | 1 |
| Exhaust | O₂ sensor | 585011/B | 1 |
| Clutch | Friction plate set | 570180/A | 1 set (6 pcs) |
| Clutch | Steel plate set | 570181/B | 1 set (5 pcs) |
| Clutch | Spring set | 570182/C | 1 set (4 pcs) |
| Brakes | Front brake pad set | 525010/A | 1 set |
| Brakes | Rear brake pad set | 525011/B | 1 set |
| Chain | Drive chain (520, 106L) | 575001/A | 1 |
| Chain | Front sprocket (15T) | 575002/B | 1 |
| Chain | Rear sprocket (42T) | 575003/C | 1 |
| Electrical | Battery (12V 9Ah) | 598050/A | 1 |
| Electrical | Regulator/Rectifier | 598051/B | 1 |
| Electrical | Stator assembly | 598052/C | 1 |

---

## 24. Warranty & Service Bulletins

### 24.1 Warranty Coverage

- **Duration**: 3 years or 40,000 km (whichever comes first).
- **Coverage**: Engine, transmission, frame, electrical system, EFI components.
- **Exclusions**: Wear items (brake pads, tyres, chain, spark plug, filters, clutch plates), accident damage, modifications.

### 24.2 Active Service Bulletins

| Bulletin No. | Date | Title | Summary |
|-------------|------|-------|---------|
| TSB-2023-001 | 2023-02-15 | Throttle Body Update | Revised cleaning procedure; new torque spec for TB bolts |
| TSB-2023-007 | 2023-06-10 | ECU Calibration v2.1 | Addresses idle surge complaint; improved cold-start enrichment |
| TSB-2024-003 | 2024-01-20 | Chain Adjuster Bolt | Replace with updated bolt (Grade 10.9) to prevent stripping |
| TSB-2024-011 | 2024-07-05 | O₂ Sensor Connector | Apply dielectric grease to prevent corrosion in humid climates |
| TSB-2025-002 | 2025-03-18 | Clutch Plate Wear Limit | Service limit revised from 2.70 mm to 2.60 mm |
| TSB-2025-009 | 2025-09-30 | ABS Module Firmware | Update to v3.1 to fix false C0035 trigger at low speed |

---

## 25. Emissions Compliance

### 25.1 BS-VI Compliance Checks

During any major service, verify the following emission-related components:

1. **Catalytic converter**: Visual inspection for damage; check with IR thermometer during warm-up (should reach 300 °C within 3 minutes of cold start).
2. **O₂ sensor**: Verify voltage swing (0.1–0.9 V) at 2,500 rpm with the scan tool live data.
3. **EVAP system** (charcoal canister): Inspect hoses for cracks or disconnection.
4. **EGR system**: Not applicable (Hunter 350 does not use EGR).
5. **PCV valve**: Check for blockage; replace if stuck.

### 25.2 Tailpipe Emission Testing

Refer to Section 7.4 for the detailed procedure.

---

## 26. Wiring Diagrams (Reference)

> 🔧 **NOTE**: Full wiring diagrams are available in the Royal Enfield Workshop Manual supplement (Part No. WD-J1C1-2024). Key circuit colours are listed below for reference.

### 26.1 Main Harness Wire Colours

| Circuit | Wire Colour |
|---------|-------------|
| Battery positive | Red (R) |
| Battery ground | Black (B) |
| Ignition switched 12 V | Red/White (R/W) |
| Headlamp high beam | Yellow (Y) |
| Headlamp low beam | Yellow/Green (Y/G) |
| Front brake lamp switch | Green/Yellow (G/Y) |
| Rear brake lamp switch | Green/White (G/W) |
| Left turn signal | Orange (O) |
| Right turn signal | Light Blue (LB) |
| Horn | Pink (P) |
| CKP sensor | White/Blue (W/BL) |
| CMP sensor | White/Green (W/G) |
| Injector | Brown/White (BR/W) |
| O₂ sensor signal | Grey (GR) |
| TPS signal | Violet (V) |
| ECT sensor | Green/Blue (G/BL) |
| IAT sensor | Light Green (LG) |

---

## 27. Glossary

| Abbreviation | Full Form |
|-------------|-----------|
| ABS | Anti-lock Braking System |
| BDC | Bottom Dead Centre |
| BS-VI | Bharat Stage VI (emission standard) |
| BTDC | Before Top Dead Centre |
| CAN | Controller Area Network |
| CKP | Crankshaft Position (sensor) |
| CMP | Camshaft Position (sensor) |
| COP | Coil-On-Plug |
| DLC | Diamond-Like Carbon (coating) |
| DOT | Department of Transportation (brake fluid standard) |
| DTC | Diagnostic Trouble Code |
| ECT | Engine Coolant Temperature (sensor) |
| ECU | Engine Control Unit |
| EFI | Electronic Fuel Injection |
| EVAP | Evaporative Emission Control |
| IAT | Intake Air Temperature (sensor) |
| ISC | Idle Speed Control |
| JASO | Japanese Automotive Standards Organization |
| MAP | Manifold Absolute Pressure (sensor) |
| MIL | Malfunction Indicator Lamp |
| OBD-II | On-Board Diagnostics, 2nd generation |
| OEM | Original Equipment Manufacturer |
| PCV | Positive Crankcase Ventilation |
| R/R | Regulator/Rectifier |
| SOHC | Single Overhead Camshaft |
| TDC | Top Dead Centre |
| TPS | Throttle Position Sensor |
| TSB | Technical Service Bulletin |
| TWC | Three-Way Catalyst |
| VIN | Vehicle Identification Number |
| VRLA | Valve-Regulated Lead-Acid (battery) |

---

## 28. Index

- **A**: ABS (Sections 15, 19, 20.5), Air Filter (5.2, 21), Alternator (10.1)
- **B**: Battery (10.2, 11.2), Brakes (15), Bearings — Steering (14.3), Bearings — Wheel (16.3)
- **C**: Cam Chain (4.4), Catalytic Converter (7.2), Chain Drive (9), Clutch (8), Compression Test (4.5), CKP Sensor (19.2)
- **D**: Diagnostic Connector (19.1), DTC Codes (19.2), Drive Chain (9)
- **E**: ECU (5.1, 19), Electrical System (10), Emissions (7, 25), Engine (4), Exhaust (7)
- **F**: Fork Service (14.1), Frame (17), Fuel Injector (5.3), Fuel Pump (5.4), Fuses (10.3)
- **G**: Gear Ratios (3.4), Gear Shift (8.3), Glossary (27)
- **H**: Handlebar (17.2), Headlamp (3.3)
- **I**: IAT Sensor (5.5), Idle Speed (20.2), Ignition (6), Instrument Cluster (18)
- **K**: Kill Switch (20.1)
- **L**: Lubrication (13)
- **M**: Maintenance Schedule (21), MAP Sensor (5.5, 19.2), MIL Lamp (18.1, 19.1)
- **N**: Neutral Indicator (18.1)
- **O**: O₂ Sensor (5.5, 7, 19.2, 25), Oil Change (13.2), Oil Pressure (13.3)
- **P**: Parts Catalog (23), Piston (4.3)
- **R**: Regulator/Rectifier (10.1)
- **S**: Safety (2), Spark Plug (6.4), Sprockets (9.3), Starter Motor (11), Suspension (14)
- **T**: Technical Specifications (3), Throttle Body (5.2), Torque Values (4.2, 17.2), TPS (5.5, 19.2), Tripper (18.2), Troubleshooting (20), Tyres (16)
- **V**: Valve Clearance (4.4), VIN (1.3), Vibration (20.4)
- **W**: Warranty (24), Wheel Bearings (16.3), Wiring Colours (26.1)

---

*End of Manual — Royal Enfield Hunter 350 Diagnostic & Service Manual, Revision 4.2*
*© Royal Enfield — For authorized service use only.*
