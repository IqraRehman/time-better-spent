import type { Config } from "tailwindcss";

export default {
  darkMode: ["class"],
  content: ["./client/index.html", "./client/src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        // Custom palette for Bee Friends Cleaners
        "honey": {
          50: "hsl(43, 96%, 95%)",
          100: "hsl(43, 96%, 90%)",
          200: "hsl(43, 96%, 80%)",
          300: "hsl(43, 96%, 70%)",
          400: "hsl(43, 96%, 63%)",
          500: "hsl(43, 96%, 56%)", // Primary honey color
          600: "hsl(43, 96%, 46%)",
          700: "hsl(43, 96%, 36%)",
          800: "hsl(43, 96%, 26%)",
          900: "hsl(43, 96%, 16%)"
        },
        "forest": {
          50: "hsl(150, 60%, 95%)",
          100: "hsl(150, 60%, 90%)",
          200: "hsl(150, 60%, 80%)",
          300: "hsl(150, 60%, 70%)",
          400: "hsl(150, 60%, 60%)",
          500: "hsl(150, 60%, 50%)",
          600: "hsl(150, 60%, 40%)",
          700: "hsl(150, 60%, 30%)",
          800: "hsl(150, 60%, 20%)",
          900: "hsl(150, 60%, 10%)"
        },
        "ocean": {
          50: "hsl(200, 65%, 95%)",
          100: "hsl(200, 65%, 90%)",
          200: "hsl(200, 65%, 80%)",
          300: "hsl(200, 65%, 70%)",
          400: "hsl(200, 65%, 60%)",
          500: "hsl(200, 65%, 50%)",
          600: "hsl(200, 65%, 40%)",
          700: "hsl(200, 65%, 30%)",
          800: "hsl(200, 65%, 20%)",
          900: "hsl(200, 65%, 10%)"
        },
        // System colors mapped to our theme
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
    },
  },
  plugins: [require("tailwindcss-animate"), require("@tailwindcss/typography")],
} satisfies Config;