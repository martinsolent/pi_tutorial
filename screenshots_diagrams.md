**1. Text‑Described Screenshots & Diagrams**

These descriptions mimic what a screenshot would show, so learners can follow along even without images.

**Screenshot 1 — Fritzing Welcome Screen**

**Description:** A large white workspace with three main panels:

- **Left panel:**  
  A vertical list of components (resistors, LEDs, breadboards, etc.).

- **Centre panel:**  
  A blank area showing “Breadboard View” with a default breadboard.

- **Right panel:**  
  A properties panel showing details of the selected component. At the top are tabs: Breadboard, Schematic, PCB, Code.

**Purpose:** Helps students recognise the interface when they first open Fritzing.

**Screenshot 2 — Selecting the Breadboard Type**

**Description:** The breadboard is highlighted with a blue outline. On the right, the Properties panel shows:

- **Type:**  
  Full / Full+ / Half

- **Rows:**  
  A–J

- **Power rails:**  
  + and –

**Purpose:** Shows where to change the breadboard to match the physical one.

**Screenshot 3 — Importing the GPIO Extension Board**

**Description:** The “Mine” section in the parts list is open. A custom GPIO extension board icon is visible. The user drags it onto the breadboard.

**Purpose:** Demonstrates how imported parts appear and how to place them.

**Screenshot 4 — Rotating and Aligning the GPIO Board**

**Description:** The GPIO board is rotated 90° anticlockwise. It is positioned so its pins sit exactly on rows E–J. The pins turn **green**, indicating correct alignment.

**Purpose:** Shows correct orientation and alignment behaviour.

**Screenshot 5 — Adding the First Jumper Wire**

**Description:** A blue wire runs from **A5** on the GPIO board to the **+ rail**. Both ends of the wire are highlighted green. The wire colour menu is open, showing colour options.

**Purpose:** Demonstrates how to create a power connection.

**Screenshot 6 — Adding the Second Jumper Wire**

**Description:** A long wire runs from **A6** to **A27**. Two bends are added so the wire avoids covering row numbers. The wire is neatly routed along the edge of the breadboard.

**Purpose:** Shows good practice for tidy diagrams.

**Screenshot 7 — Adding the Resistor and LED**

**Description:** A resistor is placed between rows 27 and 29. An LED is placed with:

- **Anode**  
  in row 29

- **Cathode**  
  in row 29 connected to the ground rail via a wire

**Purpose:** Shows the final circuit layout.

**2. Full Lesson Plan + Student Handout**

Designed for a 45–60 minute session.

**LESSON PLAN: Creating Breadboard Diagrams in Fritzing**

**Lesson Title:**

Introduction to Fritzing for Raspberry Pi Projects

**Audience:**

Beginners in electronics, computing students, hobbyists.

**Duration:**

45–60 minutes

**Learning Objectives:**

By the end of the lesson, students will be able to:

- Navigate the Fritzing interface

- Select and configure a breadboard

- Import and position a GPIO extension board

- Add jumper wires, resistors, and LEDs

- Produce a clear, tidy wiring diagram

**Materials Needed**

- Computers with Fritzing installed

- Raspberry Pi GPIO extension board (physical or image)

- Example diagram (LED + resistor circuit)

- Student handout (included below)

**Lesson Outline**

**1. Introduction (5 minutes)**

- Explain what Fritzing is and why it’s useful.

- Show examples of messy vs. tidy wiring diagrams.

- Discuss how diagrams help prevent mistakes.

**2. Exploring the Interface (5 minutes)**

Demonstrate:

- Breadboard View

- Schematic View

- PCB View

- Parts panel

- Properties panel

Use **Screenshot 1** description to guide learners.

**3. Setting Up the Breadboard (5 minutes)**

- Highlight the breadboard.

- Change the type to match the physical one.

- Rotate if needed.

Use **Screenshot 2** description.

**4. Importing and Placing the GPIO Extension (10 minutes)**

- Show how to import a custom part.

- Drag it into place.

- Rotate and align it.

Use **Screenshots 3 & 4** descriptions.

**5. Adding Jumper Wires (10 minutes)**

- Demonstrate how to drag wires from pin to pin.

- Explain snapping and green highlights.

- Show how to add bends for clarity.

Use **Screenshots 5 & 6** descriptions.

**6. Adding Components (10 minutes)**

- Add a resistor and LED.

- Explain polarity of LEDs.

- Connect ground wire.

Use **Screenshot 7** description.

**7. Review & Save (5 minutes)**

- Check alignment.

- Ensure labels are visible.

- Save the project and save imported parts.

**STUDENT HANDOUT: Fritzing Quick Guide**

**What You’re Building Today**

A simple LED circuit connected to a Raspberry Pi GPIO extension board.

**Step‑by‑Step Summary**

**1. Open Fritzing**

Go to **Breadboard View**.

**2. Choose the Correct Breadboard**

Use the Properties panel to select:

- Full / Full+ / Half

- Correct orientation

**3. Import the GPIO Extension Board**

Find it under **Mine** or import it from a file.

**4. Position the GPIO Board**

- Rotate 90° anticlockwise

- Align pins with rows E–J

- Look for green highlights

**5. Add Jumper Wires**

- A5 → + rail

- A6 → A27

- Add bends to keep the diagram tidy

**6. Add Components**

- Resistor from row 27 to 29

- LED anode to row 29

- LED cathode to ground rail

- Add a ground wire from GPIO GND to – rail

**7. Save Your Work**

Save the project and save imported parts when prompted.

**Tips for Clear Diagrams**

- Use consistent wire colours (red = power, black = ground).

- Avoid covering row numbers.

- Keep wires short and tidy.

- Check for green highlights to confirm connections.
