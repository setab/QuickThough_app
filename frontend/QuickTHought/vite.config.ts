import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    //port: 6000, // Change to the port you want to use
    //host: "127.0.0.1", // Allows access from other devices in the network (useful in WSL or remote environments)
  },
});
