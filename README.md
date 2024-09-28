# gltf_validator_connector

**gltf_validator_connector** is a script for [Archivematica](https://www.archivematica.org/) that uses the official [glTF-Validator](https://github.com/KhronosGroup/glTF-Validator/releases) tool to validate glTF files.

## Installation

To install the **gltf_validator_connector** script in Archivematica, follow these steps:

### 1. Download the official glTF-Validator tool 

- Download the latest release of the [glTF-Validator](https://github.com/KhronosGroup/glTF-Validator/releases) and install it in the `"/usr/share/"` folder.

### 2. Create a new format policy tool
- In the Archivematica frontend, navigate to **Preservation planning** > **Format policy registry** > **Tools** > **Create new tool** or go directly to [this link](http://10.10.10.20/fpr/fptool/create/).
- Enter the following parameters:
    - **Description**: Enter `"gltf_validator"`.
    - **Version**: Enter `"1.0"`.
- Click **Save**.

### 3. Create a new validation command
- In the Archivematica frontend, navigate to **Preservation planning** > **Validation** > **Commands** > **Create new command** or go directly to [this link](http://10.10.10.20/fpr/idcommand/create/).
- Fill in the following fields:
    - **The related tool**: Select **gltf_validator**.
    - **Description**: Enter `"Identify using gltf_validator"`.
    - **Script**: Paste the entire content of the **gltf_validator_connector.py** file.
    - **Script type**: Select **Python script**.
    - **Command usage**: Select **Validation**.
- Click **Save**.

### 4. Create a new validation rule for ASCII based glTF 1.0
- In the Archivematica frontend, navigate to **Preservation planning** > **Validation** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
    - **Purpose**: Select **Validation**.
    - **The related format**: Select **Model: GL Transmission Format (Text): GLTF 1.0 (fmt/1314)**.
    - **Command**: Select **Validate using gltf_validator**.
- Click **Save**.

### 5. Create a new validation rule for ASCII based glTF 2.0
- In the Archivematica frontend, navigate to **Preservation planning** > **Validation** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
    - **Purpose**: Select **Validation**.
    - **The related format**: Select **Model: GL Transmission Format (Text): GLTF 2.0 (fmt/1315)**.
    - **Command**: Select **Validate using gltf_validator**.
- Click **Save**.

### 6. Create a new validation rule for binary glTF files
- In the Archivematica frontend, navigate to **Preservation planning** > **Validation** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
    - **Purpose**: Select **Validation**.
    - **The related format**: Select **Model: GL Transmission Format (Binary): GLTF (Binary) (fmt/1316)**.
    - **Command**: Select **Validate using gltf_validator**.
- Click **Save**.

## Dependencies

[Archivematica 1.13.2](https://github.com/artefactual/archivematica/releases/tag/v1.13.2) and [glTF-Validator 2.0.0-dev.3.8](https://github.com/KhronosGroup/glTF-Validator/releases/tag/2.0.0-dev.3.8) were used to analyze, design, develop and test this script.

## Background

As part of the [NFDI4Culture](https://nfdi4culture.de/) initiative, efforts are being made to enhance the ability of open-source digital preservation software like Archivematica to identify, validate and preserve 3D file formats. This repository provides the **gltf_validator_connector** script that allows validating glTF files in Archivematica based on the official [glTF-Validator](https://github.com/KhronosGroup/glTF-Validator/releases) tool. 

By default, Archivematica 1.13.2 can not validate glTF files at all. Now, with the **gltf_validator_connector** glTF files can be validated, ensuring better support for the preservation of 3D files in Archivematica.

## Imprint

[NFDI4Culture](https://nfdi4culture.de/) – Consortium for Research Data on Material and Immaterial Cultural Heritage

NFDI4Culture is a consortium within the German [National Research Data Infrastructure (NFDI)](https://www.nfdi.de/).

Author: [Jörg Heseler](https://orcid.org/0000-0002-1497-627X)

This project is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

NFDI4Culture is funded by the German Research Foundation (DFG) – Project number – [441958017](https://gepris.dfg.de/gepris/projekt/441958017).