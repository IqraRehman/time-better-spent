import { pgTable, text, serial, integer } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod";

export const houses = pgTable("houses", {
  id: serial("id").primaryKey(),
  squareFeet: integer("square_feet").notNull(),
  bedrooms: integer("bedrooms").notNull(),
  bathrooms: integer("bathrooms").notNull(),
  calculatedMinutes: integer("calculated_minutes").notNull(),
});

export const insertHouseSchema = createInsertSchema(houses).pick({
  squareFeet: true,
  bedrooms: true,
  bathrooms: true,
  calculatedMinutes: true,
}).extend({
  squareFeet: z.number()
    .min(500, "House must be at least 500 square feet - this is our minimum size for calculation")
    .max(10000, "Wow, that's a mansion! Please double-check your square footage - we typically handle homes under 10,000 square feet"),
  bedrooms: z.number()
    .min(1, "House must have at least 1 bedroom")
    .max(5, "That's a lot of bedrooms! Please verify your input - we typically handle homes with 5 or fewer bedrooms"),
  bathrooms: z.number()
    .min(1, "House must have at least 1 bathroom")
    .max(6, "That's a lot of bathrooms! Please verify your input - we typically handle homes with 6 or fewer bathrooms"),
});

export type InsertHouse = z.infer<typeof insertHouseSchema>;
export type House = typeof houses.$inferSelect;