import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { type Activity } from "@shared/activities";

interface ActivityCardProps {
  activity: Activity;
  hoursAvailable: number;
}

export default function ActivityCard({ activity, hoursAvailable }: ActivityCardProps) {
  const possibleUnits = Math.floor(hoursAvailable / activity.timePerUnit);
  
  return (
    <Card className="overflow-hidden">
      <div 
        className="h-48 bg-cover bg-center"
        style={{ backgroundImage: `url(${activity.imageUrl})` }}
      />
      <CardHeader>
        <CardTitle>{activity.title}</CardTitle>
      </CardHeader>
      <CardContent>
        <p className="text-muted-foreground mb-4">{activity.description}</p>
        <p className="text-lg font-semibold">
          In this time you could complete{" "}
          <span className="text-primary">{possibleUnits} {activity.unit}</span>
        </p>
      </CardContent>
    </Card>
  );
}
