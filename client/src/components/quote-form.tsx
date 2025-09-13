import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { useState } from "react";
import { Check, Loader2 } from "lucide-react";
import { useToast } from "@/hooks/use-toast";

// TODO: Implement hCaptcha verification once site key is set up
// import HCaptcha from '@hcaptcha/react-hcaptcha';

const quoteFormSchema = z.object({
  name: z.string().min(2, "Please enter your name"),
  email: z.string().email("Please enter a valid email"),
  zipCode: z.string().regex(/^\d{5}$/, "Please enter a valid 5-digit zip code"),
  squareFeet: z.number()
    .min(500, "House must be at least 500 square feet")
    .max(10000, "Please verify square footage - we typically handle homes under 10,000 square feet"),
  bedrooms: z.number()
    .min(1, "House must have at least 1 bedroom")
    .max(10, "Please verify the number of bedrooms"),
  bathrooms: z.number()
    .min(1, "House must have at least 1 bathroom")
    .max(10, "Please verify the number of bathrooms")
});

type QuoteFormData = z.infer<typeof quoteFormSchema>;

interface QuoteFormProps {
  initialValues?: {
    squareFeet: number;
    bedrooms: number;
    bathrooms: number;
  };
}

export default function QuoteForm({ initialValues }: QuoteFormProps) {
  const [submitted, setSubmitted] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const { toast } = useToast();

  const form = useForm<QuoteFormData>({
    resolver: zodResolver(quoteFormSchema),
    defaultValues: {
      squareFeet: initialValues?.squareFeet || 2300,
      bedrooms: initialValues?.bedrooms || 3,
      bathrooms: initialValues?.bathrooms || 2
    }
  });

  async function onSubmit(data: QuoteFormData) {
    try {
      setIsSubmitting(true);
      console.log("Submitting form data:", data);
      const response = await fetch('/api/request-quote', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.details || 'Failed to submit quote request');
      }

      setSubmitted(true);
    } catch (error) {
      console.error('Error submitting form:', error);
      toast({
        title: "Error",
        description: error instanceof Error ? error.message : "Failed to submit quote request. Please try again.",
        variant: "destructive"
      });
    } finally {
      setIsSubmitting(false);
    }
  }

  if (submitted) {
    return (
      <div className="text-center p-6 bg-primary/5 rounded-lg">
        <Check className="w-12 h-12 text-primary mx-auto mb-4" />
        <h3 className="text-xl font-semibold mb-2">Thank You!</h3>
        <p>
          We'll send your free quote and $40 off coupon to your email shortly.
          Check your inbox!
        </p>
      </div>
    );
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
        <FormField
          control={form.control}
          name="name"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Name</FormLabel>
              <FormControl>
                <Input placeholder="Enter your name" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name="email"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Email</FormLabel>
              <FormControl>
                <Input placeholder="you@example.com" type="email" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name="zipCode"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Zip Code</FormLabel>
              <FormControl>
                <Input placeholder="12345" maxLength={5} {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        {/* Hidden fields for house details */}
        <input type="hidden" {...form.register("squareFeet", { valueAsNumber: true })} />
        <input type="hidden" {...form.register("bedrooms", { valueAsNumber: true })} />
        <input type="hidden" {...form.register("bathrooms", { valueAsNumber: true })} />

        <Button type="submit" className="w-full" disabled={isSubmitting}>
          {isSubmitting ? (
            <>
              <Loader2 className="w-4 h-4 mr-2 animate-spin" />
              Sending...
            </>
          ) : (
            "Get My Free Quote + $40 Off Coupon"
          )}
        </Button>
      </form>
    </Form>
  );
}