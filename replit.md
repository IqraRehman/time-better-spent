# replit.md

## Overview

This is a full-stack web application called "Time Better Spent" that helps users calculate how much time they spend cleaning their homes and suggests alternative activities they could do instead. The app takes house specifications (square footage, bedrooms, bathrooms) as input, calculates cleaning time, and presents creative activity suggestions to inspire users to hire cleaning services rather than clean themselves. The application includes a quote request system with email notifications and social sharing features to promote a cleaning service with discount codes.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

**Frontend Architecture:**
- React-based single-page application using TypeScript
- Vite as the build tool and development server
- Wouter for client-side routing (lightweight alternative to React Router)
- TanStack Query for server state management and API calls
- React Hook Form with Zod validation for form handling
- Tailwind CSS for styling with custom color palette (honey, forest, ocean themes)
- Shadcn/ui component library built on Radix UI primitives
- Framer Motion for animations and transitions

**Backend Architecture:**
- Express.js server with TypeScript
- RESTful API design with endpoints for calculations and quote requests
- In-memory storage using a custom storage abstraction layer (MemStorage class)
- Middleware for request logging and error handling
- Development-only Vite integration for hot module replacement

**Database Design:**
- Drizzle ORM configured for PostgreSQL with schema migrations
- House calculation schema with fields for square footage, bedrooms, bathrooms, and calculated minutes
- Current implementation uses in-memory storage but is architected to easily switch to PostgreSQL

**Form Validation & Data Flow:**
- Zod schemas for type-safe validation on both client and server
- Shared schema definitions between frontend and backend
- Input validation with user-friendly error messages
- Form state management with React Hook Form

**Activity Recommendation System:**
- Predefined activity database with time requirements and categorization
- Algorithm to match user's available time (calculated from cleaning estimate) with suitable activities
- Activity cards with images, descriptions, and time estimates

**Quote Request System:**
- Contact form with validation for name, email, zip code, and house details
- SendGrid integration for email notifications
- hCaptcha integration prepared (but not fully implemented)

**Social Sharing Features:**
- Native Web Share API support with fallback to social media buttons
- Share buttons for Twitter, Facebook, LinkedIn, and WhatsApp
- Promotional messaging with discount codes embedded in shared content

**Development & Build Pipeline:**
- TypeScript throughout the entire stack
- ESBuild for server-side bundling
- Vite plugins for theme management and development tools
- PostCSS with Tailwind CSS processing
- Path aliases for clean imports (@/ for client, @shared/ for shared code)

**State Management:**
- TanStack Query for server state and API caching
- React Hook Form for form state
- Component-level state with React hooks
- Toast notifications for user feedback

**Responsive Design:**
- Mobile-first Tailwind CSS approach
- Custom hook for mobile detection
- Responsive component variants throughout the UI

**Error Handling:**
- Global error boundary in Express middleware
- Client-side error handling with toast notifications
- Form validation errors with field-level messaging
- API response error handling with user-friendly messages

## External Dependencies

**Database & Storage:**
- Drizzle ORM with PostgreSQL support (@neondatabase/serverless)
- Connection pooling configured for Neon Database
- Environment variable configuration for database URL

**Email Services:**
- SendGrid for transactional email delivery
- API key authentication required
- Quote request notifications to business email

**UI Component Libraries:**
- Radix UI primitives for accessible component foundations
- Shadcn/ui component system
- Lucide React for consistent iconography
- React Share for social media sharing functionality

**Form & Validation:**
- React Hook Form for performant form handling
- Zod for schema validation and type inference
- @hookform/resolvers for integration between the two

**Development Tools:**
- Replit-specific plugins for theme management and development experience
- Vite ecosystem plugins for enhanced development workflow

**Security & Verification:**
- hCaptcha integration prepared for bot protection (requires site key configuration)
- Input sanitization through Zod validation schemas

**Deployment & Runtime:**
- Node.js runtime with ES modules
- Environment variables for configuration
- Production build optimization with Vite and ESBuild