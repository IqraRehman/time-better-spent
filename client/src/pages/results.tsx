import { useQuery } from "@tanstack/react-query";
import { useParams, Link } from "wouter";
import { findMatchingActivities } from "@shared/activities";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ExternalLink } from "lucide-react";
import ShareButtons from "@/components/share-buttons";
import QuoteForm from "@/components/quote-form";

export default function Results() {
  const { id } = useParams();
  const { data: house, isLoading } = useQuery({
    queryKey: [`/api/calculation/${id}`],
  });

  if (isLoading) {
    return <div className="p-8 text-center">Loading...</div>;
  }

  if (!house) {
    return <div className="p-8 text-center">Calculation not found</div>;
  }

  const monthlyHours = (house.calculatedMinutes / 60) * 4;
  const matchingActivities = findMatchingActivities(monthlyHours);
  const activity = matchingActivities[0];

  if (!activity) {
    return (
      <div className="p-8 text-center">
        <h2 className="text-2xl font-bold">No matching activities found</h2>
        <p className="mt-4">Try adjusting your house details for different suggestions.</p>
        <Link href="/">
          <Button className="mt-4">Try Again</Button>
        </Link>
      </div>
    );
  }

  const shareUrl = typeof window !== 'undefined' ? window.location.href : '';
  const shareTitle = `${activity.title} - Time Better Spent`;
  const shareDescription = `Instead of spending ${Math.round(monthlyHours)} hours cleaning each month, I'm going to ${activity.title.toLowerCase()}!`;

  return (
    <div className="min-h-screen bg-gradient-to-b from-primary/10 to-background p-4">
      <div className="max-w-3xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-8 pt-8"
        >
          <h1 className="text-4xl font-bold mb-4">
            Instead of spending {Math.round(monthlyHours)} hours cleaning each month...
          </h1>
          <p className="text-muted-foreground text-lg mb-8">
            Here's something amazing you could do!
          </p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.5 }}
        >
          <Card className="overflow-hidden">
            <div
              className="h-64 bg-cover bg-center"
              style={{ backgroundImage: `url(${activity.imageUrl})` }}
            />
            <CardHeader>
              <CardTitle className="text-3xl">{activity.title}</CardTitle>
            </CardHeader>
            <CardContent className="space-y-6">
              <p className="text-xl text-muted-foreground">
                {activity.description}
              </p>

              <div className="bg-primary/5 p-6 rounded-lg">
                <p className="text-lg font-medium text-primary mb-2">
                  Time Investment:
                </p>
                <p className="text-muted-foreground">
                  {activity.timeRequirement.minHours}-{activity.timeRequirement.maxHours} hours total
                </p>
              </div>

              <div className="prose prose-lg">
                <h3 className="text-2xl font-semibold text-primary mb-4">
                  Your Journey
                </h3>
                <div className="whitespace-pre-line">
                  {activity.detailedTimeline}
                </div>
              </div>

              {activity.resources && activity.resources.length > 0 && (
                <div className="bg-primary/5 p-6 rounded-lg">
                  <h4 className="text-lg font-medium text-primary mb-4">
                    Resources to Get Started:
                  </h4>
                  <ul className="space-y-2">
                    {activity.resources.map((resource, index) => {
                      const [url, description] = resource.split(" - ");
                      return (
                        <li key={index} className="flex items-start gap-2">
                          <ExternalLink className="w-4 h-4 mt-1 flex-shrink-0" />
                          <a
                            href={url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="text-primary hover:underline"
                          >
                            {description}
                          </a>
                        </li>
                      );
                    })}
                  </ul>
                </div>
              )}

              <div className="bg-primary/10 p-6 rounded-lg mt-6">
                <div className="mb-6">
                  <h3 className="text-2xl font-semibold text-primary mb-2">
                    Ready to Get Started?
                  </h3>
                  <p className="text-muted-foreground mb-4">
                    Get your house professionally cleaned and use your free time for {activity.title.toLowerCase()}!
                    Get a free quote now and receive a special $40 off coupon.
                  </p>
                </div>
                <QuoteForm
                  initialValues={{
                    squareFeet: house.squareFeet,
                    bedrooms: house.bedrooms,
                    bathrooms: house.bathrooms
                  }}
                />
                <div className="mt-6 pt-6 border-t">
                  <p className="text-lg font-medium text-primary mb-4">
                    🎉 Spread the Joy! Help Friends Reclaim Their Time
                  </p>
                  <p className="text-sm text-muted-foreground mb-6">
                    Found an amazing alternative to cleaning? Share your discovery and special $40 off coupon with friends who could use more time for {activity.title.toLowerCase()}! Together, let's transform cleaning hours into moments of joy.
                  </p>
                  <ShareButtons
                    title={shareTitle}
                    description={shareDescription}
                    url={shareUrl}
                  />
                </div>
              </div>
            </CardContent>
          </Card>
        </motion.div>

        <div className="text-center mt-8">
          <Link href="/">
            <Button size="lg" variant="outline" className="mr-4">
              Calculate Again
            </Button>
          </Link>
          <Button size="lg" className="bg-primary">
            Schedule Cleaning
          </Button>
        </div>
      </div>
    </div>
  );
}