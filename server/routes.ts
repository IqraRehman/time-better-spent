import type { Express } from "express";
import { createServer } from "http";
import { storage } from "./storage";
import { insertHouseSchema } from "@shared/schema";
import sgMail from "@sendgrid/mail";

if (!process.env.SENDGRID_API_KEY) {
  console.error("SENDGRID_API_KEY is not set!");
}
sgMail.setApiKey(process.env.SENDGRID_API_KEY!);

export async function registerRoutes(app: Express) {
  app.post("/api/calculate", async (req, res) => {
    const result = insertHouseSchema.safeParse(req.body);
    if (!result.success) {
      return res.status(400).json({ error: "Invalid input" });
    }

    const hoursPerClean =
      (result.data.squareFeet / 750) + // 1 hour per 750 sq ft
      (result.data.bedrooms * 0.333) + // 20 mins per bedroom
      (result.data.bathrooms * 0.333); // 20 mins per bathroom

    const calculatedMinutes = Math.round(hoursPerClean * 60);

    const house = await storage.createHouseCalculation({
      ...result.data,
      calculatedMinutes,
    });

    res.json(house);
  });

  app.get("/api/calculation/:id", async (req, res) => {
    const id = parseInt(req.params.id);
    if (isNaN(id)) {
      return res.status(400).json({ error: "Invalid ID" });
    }

    const house = await storage.getHouseCalculation(id);
    if (!house) {
      return res.status(404).json({ error: "Not found" });
    }

    res.json(house);
  });

  app.post("/api/request-quote", async (req, res) => {
    try {
      console.log("Received quote request:", req.body);
      const { name, email, zipCode, squareFeet, bedrooms, bathrooms } = req.body;

      // Validate required fields
      if (!name || !email || !zipCode || !squareFeet || !bedrooms || !bathrooms) {
        return res.status(400).json({ error: "Missing required fields" });
      }

      // TODO: Implement hCaptcha verification once site key is set up
      // The verification code will be added here later

      // Use the verified domain email
      const senderEmail = "noreply@em6757.beefriendcleaner.com";

      try {
        // Send email to customer service team
        await sgMail.send({
          to: "service@beefriendscleaners.com",
          from: senderEmail,
          subject: "New Cleaning Quote Request",
          html: `
            <h2>New Quote Request</h2>
            <p>Customer Details:</p>
            <ul>
              <li>Name: ${name}</li>
              <li>Email: ${email}</li>
              <li>Zip Code: ${zipCode}</li>
            </ul>
            <p>House Details:</p>
            <ul>
              <li>Square Feet: ${squareFeet}</li>
              <li>Bedrooms: ${bedrooms}</li>
              <li>Bathrooms: ${bathrooms}</li>
            </ul>
            <p>This lead came from our Time Better Spent calculator tool.</p>
          `,
        });

        // Send confirmation email to client
        await sgMail.send({
          to: email,
          from: senderEmail,
          subject: "Your Free Quote + $40 Off Coupon",
          html: `
            <h2>Thank You for Choosing Bee Friends Cleaners!</h2>
            <p>Dear ${name},</p>
            <p>Thank you for using our Time Better Spent calculator and requesting a quote. Our team will review your home details and send you a personalized cleaning quote by the end of the day.</p>
            <p>As a special thank you, we're including a $40 off coupon with your first cleaning service!</p>
            <p>House Details We'll Be Quoting:</p>
            <ul>
              <li>${squareFeet} square feet</li>
              <li>${bedrooms} bedrooms</li>
              <li>${bathrooms} bathrooms</li>
            </ul>
            <p>If you have any questions in the meantime, please don't hesitate to reach out.</p>
            <p>Best regards,<br>Your Friends at Bee Friends Cleaners</p>
          `,
        });

        res.json({ success: true });
      } catch (emailError: any) {
        console.error("SendGrid error details:", emailError.response?.body);
        throw new Error(`Email sending failed: ${emailError.message}`);
      }
    } catch (error) {
      console.error("Error processing quote request:", error);
      res.status(500).json({ 
        error: "Failed to process quote request",
        details: error instanceof Error ? error.message : "Unknown error"
      });
    }
  });

  return createServer(app);
}