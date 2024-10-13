# Simple File Storage Server

A simple file storage server built with FastAPI that allows users to upload, delete, and list files via a REST API. Additionally, a command-line interface (CLI) is provided for easier interaction with the server.

## Features

- Upload files to the server
- Delete files from the server
- List all uploaded files
- CLI for easier interaction with the server

## Installation

### Windows

1. Clone the repository:

   ```cmd
   git clone https://github.com/abtinfi/simple-file-storage-server.git
   cd simple-file-storage-server
   ```

2. Create a virtual environment and activate it:

   ```cmd
   python -m venv myenv
   myenv\Scripts\activate
   ```

3. Install the dependencies:

   ```cmd
   pip install -r requirements.txt
   ```

### Linux / macOS

1. Clone the repository:

   ```bash
   git clone https://github.com/abtinfi/simple-file-storage-server.git
   cd simple-file-storage-server
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Server

To start the FastAPI server:

```bash
uvicorn main:app --reload
```

The server will run at `http://127.0.0.1:8000`.

### Using the CLI

The CLI provides an easy way to interact with the server. You can use it to upload, delete, and list files.

1. **Upload a file:**

   ```bash
   python cli.py upload-file <file_path> <file_name>
   ```
   - `<file_path>`: Path to the file on your local system.
   - `<file_name>`: Desired name for the file on the server.

2. **Delete a file:**

   ```bash
   python cli.py delete-file <file_name>
   ```
   - `<file_name>`: Name of the file to delete from the server.

3. **List all files:**

   ```bash
   python cli.py list-files
   ```

## Docker Deployment

1. Build and run the Docker container:

   ```bash
   docker-compose up --build
   ```

2. The server will be available at `http://localhost:8000`.

## API Endpoints

- **Upload a file:** `POST /files/{name}`
- **Delete a file:** `DELETE /files/{name}`
- **List all files:** `GET /files`


## Live Demo
Access the live server [here](https://simple-file-storage-server.onrender.com).
