Mission Control
├── Positioning & Navigation
│   ├── INS
│   ├── USBL
│   └── GNSS
│
├── Acoustic Sensors
│   ├── MBES
│   ├── SSS
│   └── SBP
│
├── Environmental Sensors  ← SVP LIVES HERE
│   ├── SVP (Sound Velocity Profiler)
│   │   ├── Status: Last cast time, current profile applied
│   │   ├── Control: Trigger new cast, import profile
│   │   └── Validation: Profile age, depth coverage
│   └── CTD (if applicable)
│
└── Visual Systems
    ├── Cameras
    └── Lighting
```

### Why "Environmental Sensors" Category?

The SVP measures **environmental conditions** (water column sound velocity) that affect **acoustic sensor performance**. It's not a data acquisition sensor itself, but a calibration/correction input.

---

## SVP-Specific Interfaces Across Screens

### **Screen 2 (Mission Control):**
**SVP Control Panel:**
```
┌─────────────────────────────────────┐
│ SVP - Sound Velocity Profiler      │
├─────────────────────────────────────┤
│ Status: ✓ Profile Applied           │
│ Last Cast: 08:45 (2h 15m ago)      │
│ Profile: SVP_20250127_0845.csv     │
│                                     │
│ [Trigger New Cast] [Import Profile] │
│                                     │
│ ⚠ Profile Age Warning: >2 hours     │
│   Recommend new cast before Line 6  │
└─────────────────────────────────────┘
```

### **Screen 6 (QC Dashboard):**
**SVP Impact Monitoring:**
```
┌─────────────────────────────────────┐
│ Sound Velocity Status               │
├─────────────────────────────────────┤
│ Current Profile: Valid ✓            │
│ Depth Coverage: 0-500m              │
│ Survey Depth: 245m (within range)   │
│                                     │
│ MBES Ray-tracing: Using SVP_0845    │
│ TPU Impact: ±0.15m (acceptable)    │
└─────────────────────────────────────┘
```

### **Screen 3 (Navigation):**
**Optional SVP Context:**
- Small indicator showing "SVP: Current" or "SVP: Outdated"
- Link to trigger new cast from navigation context

---

## SVP in the Signal Flow Diagram

When users access the **Interactive Signal Flow** (diagnostic view), SVP appears as:
```
┌──────┐    ┌─────┐    ┌──────────┐
│ SVP  │───→│ SIS │───→│   MBES   │
└──────┘    └─────┘    └──────────┘
            (applies     (corrected
            velocity     depths)
            profile)
```

**Interaction:** Click SVP node → Shows:
- Profile metadata (time, depth range, source)
- Validation status
- Quick actions (re-cast, import)

---

## SVP-Related Requirements (Adding to our list)

**REQ-CC-018**: System SHALL enable triggering SVP casts with timestamp and geolocation auto-logging

**REQ-CC-019**: System SHALL import and validate external SVP profiles (CSV, manufacturer formats)

**REQ-CC-020**: System SHALL alert when SVP profile age exceeds configurable threshold (default: 4 hours)

**REQ-AM-024**: System SHALL display SVP profile application status in QC dashboard

**REQ-AM-025**: System SHALL validate SVP depth coverage against current survey depth

**REQ-AM-026**: System SHALL highlight MBES data quality impacts when SVP profile is outdated or invalid

**REQ-TL-013**: System SHALL auto-log all SVP cast events (trigger time, profile application, validation results)

---

## SVP Workflow Integration

### Typical SVP Interaction Pattern:

**Pre-Mission Setup:**
1. Operator loads mission template
2. System checks: "No SVP profile loaded" → Amber alert
3. Operator triggers SVP cast OR imports recent profile
4. System validates and applies → Green status

**During Operations:**
1. System monitors profile age
2. At 3-hour mark: Info notification "SVP profile aging"
3. At 4-hour mark: Warning alert "Recommend new SVP cast"
4. At line end or opportune moment: Operator triggers new cast
5. Auto-log: "11:23 - SVP cast initiated (Line 5 complete)"

**Multi-Mission Consideration:**
- Each mission can use **different SVP profiles** (if operating in different areas/depths)
- OR **share a common profile** (if missions in same water body)
- System tracks which profile is applied to which mission's MBES data

---

## Configuration & Templates

**SVP in Mission Templates:**
```
Pipeline Inspection Template (North Sea)
├── Sensors
├── Positioning
└── Environmental
    └── SVP Settings
        ├── Auto-cast interval: 4 hours
        ├── Depth range required: 0-300m
        ├── Alert threshold: 3 hours
        └── Validation: Check against survey depth