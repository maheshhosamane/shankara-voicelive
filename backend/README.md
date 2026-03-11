# Shankara Voice Live Backend Setup Instructions

## Prerequisites
- Node.js (version 14 or higher)
- npm (Node Package Manager)
- MongoDB (for database management)

## Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/maheshhosamane/shankara-voicelive.git
   ```
2. Navigate into the project directory:
   ```bash
   cd shankara-voicelive
   ```
3. Install the required dependencies:
   ```bash
   npm install
   ```

## Environment Configuration
1. Create a `.env` file in the root directory of the project:
   ```bash
   touch .env
   ```
2. Add the following environment variables:
   ```plaintext
   PORT=3000
   MONGO_URI=<your_mongodb_connection_string>
   JWT_SECRET=<your_jwt_secret>
   ```

## How to Run the Server
- To start the server, run:
  ```bash
  npm start
  ```
- The server will be running on `http://localhost:3000`.

## Troubleshooting Guide
- **Common Issues**:
  - `Error: Cannot find module 'xyz'`: Ensure all dependencies are installed.
  - `Connection refused`: Check your MongoDB connection string and database status.
  - If you encounter any other issues, check the logs for more details.

## Additional Notes
- Make sure to have `git` installed on your system to clone the repository. Keep your Node.js and npm versions updated for smoother performance.
- For any other inquiries, refer to the GitHub issues for this repository or contact the repository owner.