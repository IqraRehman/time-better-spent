import { Card, CardContent } from "@/components/ui/card";
import HouseForm from "@/components/house-form";
import { motion } from "framer-motion";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-primary/10 to-background p-4">
      <div className="max-w 2xl mx-auto">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="text-center mb-8 pt-8"
        >
          <h1 className="text-4xl font-bold bg-gradient-to-r from-primary to-primary/60 text-transparent bg-clip-text mb-4">
            Time Better Spent
          </h1>
          <p className="text-muted-foreground text-lg">
            See what amazing things you could do instead of cleaning your house
          </p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.5, delay: 0.2 }}
        >
          <Card className="max-w-xl mx-auto">
            <CardContent className="pt-6">
              <HouseForm />
            </CardContent>
          </Card>
        </motion.div>
      </div>
    </div>
  );
}
