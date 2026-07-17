import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// /api istekleri backend'e (port 8000) yönlendirilir — CORS derdi olmadan.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": "http://localhost:8000",
    },
  },
});
