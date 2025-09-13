import { Share2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  TwitterShareButton,
  FacebookShareButton,
  LinkedinShareButton,
  WhatsappShareButton,
  TwitterIcon,
  FacebookIcon,
  LinkedinIcon,
  WhatsappIcon,
} from 'react-share';

interface ShareButtonsProps {
  title: string;
  description: string;
  url: string;
}

export default function ShareButtons({ title, description, url }: ShareButtonsProps) {
  const handleNativeShare = async () => {
    try {
      await navigator.share({
        title,
        text: description + "\n\n✨ Join me and get $40 off your first cleaning with code TAKE40OFF!",
        url,
      });
    } catch (error) {
      console.error('Error sharing:', error);
    }
  };

  // Format share text consistently across platforms
  const shareText = `✨ I just discovered something amazing! Instead of cleaning, I'm going to ${title.toLowerCase()}!\n\n${description}\n\n🎁 Want to try it too? Use code TAKE40OFF for $40 off your first cleaning and find your perfect activity at:`;

  const hashTags = ['TimeBetterSpent', 'LifeHack', 'TAKE40OFF'];

  return (
    <div className="flex flex-col items-center gap-4">
      {/* Native Share Button - only show if the API is available */}
      {(typeof navigator !== 'undefined' && 'share' in navigator) && (
        <Button 
          onClick={handleNativeShare}
          variant="outline"
          className="w-full flex items-center gap-2 bg-primary/5 hover:bg-primary/10"
        >
          <Share2 className="w-4 h-4" />
          Share Your Discovery + $40 Off Code
        </Button>
      )}

      {/* Social Media Share Buttons */}
      <div className="flex gap-3 justify-center">
        <TwitterShareButton url={url} title={shareText} hashtags={hashTags}>
          <TwitterIcon size={36} round className="hover:opacity-80 transition-opacity" />
        </TwitterShareButton>

        <FacebookShareButton url={url} hashtag={`#${hashTags[0]}`} quote={shareText}>
          <FacebookIcon size={36} round className="hover:opacity-80 transition-opacity" />
        </FacebookShareButton>

        <LinkedinShareButton 
          url={url} 
          title={title}
          summary={`${description}\n\n✨ Get $40 off your first cleaning with code TAKE40OFF and discover your perfect alternative activity!`}
          source="Time Better Spent"
        >
          <LinkedinIcon size={36} round className="hover:opacity-80 transition-opacity" />
        </LinkedinShareButton>

        <WhatsappShareButton url={url} title={shareText}>
          <WhatsappIcon size={36} round className="hover:opacity-80 transition-opacity" />
        </WhatsappShareButton>
      </div>

      <p className="text-sm text-muted-foreground mt-4">
        Share the joy of time better spent and help friends discover their perfect alternative! 🌟
      </p>
    </div>
  );
}