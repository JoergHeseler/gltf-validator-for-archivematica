# glTF Validator for Archivematica

This repository provides a script that uses the official [glTF-Validator](https://github.com/KhronosGroup/glTF-Validator/releases) tool to validate Graphics Language Transmission Format (glTF) files in [Archivematica](https://www.archivematica.org/).

## Installation

To install this script, follow these steps:

### 1. Download the official glTF-Validator tool

- Download the latest release of the [glTF-Validator](https://github.com/KhronosGroup/glTF-Validator/releases) and install it in the `/usr/share/` folder.

### 2. Create a new format policy tool

- In the Archivematica frontend, navigate to **Preservation planning** > **Format policy registry** > **Tools** > **Create new tool** or go directly to [this link](http://10.10.10.20/fpr/fptool/create/).
- Enter the following parameters:
  - **Description**: Enter `gltf_validator`.
  - **Version**: Enter the version you downloaded, e. g. `2.0.0-dev.3.8`.
- Click **Save**.

### 3. Create a new validation command

- In the Archivematica frontend, navigate to **Preservation planning** > **Validation** > **Commands** > **Create new command** or go directly to [this link](http://10.10.10.20/fpr/fpcommand/create/).
- Fill in the following fields:
  - **The related tool**: Select **gltf_validator**.
  - **Description**: Enter `Validate using gltf_validator`.
  - **Command**: Paste the entire content of the [**gltf-validator.py**](./src/gltf-validator.py) file.
  - **Script type**: Select **Python script**.
  - **Command usage**: Select **Validation**.
  - Leave all other input fields and combo boxes untouched.
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

## Test

To test this validator, you can use the sample glTF files located [here](https://github.com/JoergHeseler/mesh-samples-for-preservation-testing/tree/main/gltf).

### In Archivematica:

You can view the error codes and detailed validation results in the Archivmatica frontend after starting a transfer by expanding the `▸ Microservice: Validation` section and clicking on the gear icon of `Job: Validate formats`.

Files with no errors end with `valid` in their name and should pass validation with this script (i. e. return error code **0**). However, all other files contain errors and should fail validation (i. e. return error code **1**).

### In the command line:

You can use the validator at the command line prompt by typing `python gltf-validator.py <GLTF file to validate>`. You may also want to add `--validator-path=<path to the official gltf_validator>`.

## Dependencies

[Archivematica 1.13.2](https://github.com/artefactual/archivematica/releases/tag/v1.13.2) and [glTF-Validator 2.0.0-dev.3.8](https://github.com/KhronosGroup/glTF-Validator/releases/tag/2.0.0-dev.3.8) were used to analyze, design, develop and test this script.

## Background

As part of the [NFDI4Culture](https://nfdi4culture.de/) initiative, efforts are underway to enhance the capabilities of open-source digital preservation software like Archivematica to identify, validate and preserve 3D file formats. This repository provides a script to enable Graphics Language Transmission Format (glTF) file validation in Archivematica, which is not supported by default in version 1.13.2, enhancing its 3D content preservation capabilities.

## Related Projects

- [NFDI4Culture 3D Reference Implementations](https://github.com/JoergHeseler/nfdi4culture-3d-reference-implementations)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgments

Special thanks to the colleagues from the SLUB Dresden, specifically from the Infrastructure and Long-Term Availability division, for their support and valuable feedback during the development.

## Imprint

[NFDI4Culture](https://nfdi4culture.de/) – Consortium for Research Data on Material and Immaterial Cultural Heritage.  
Funded by the German Research Foundation (DFG), Project No. [441958017](https://gepris.dfg.de/gepris/projekt/441958017).

**Author**: [Jörg Heseler](https://orcid.org/0000-0002-1497-627X)  
**License**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
