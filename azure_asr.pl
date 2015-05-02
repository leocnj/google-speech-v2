#!/usr/bin/perl
#
# based on http://bit.ly/10b6jx9
#
# TODO: convert to a Python version using urllib2
#
# 5/1/2015  make this work for the new MSFT Bing ASR API.
#
require LWP::UserAgent;

my $url = "https://speech.platform.bing.com/recognize";
my $audio = "";

open(FILE, "<" . $ARGV[0]);
while(<FILE>)
{
    $audio .= $_;
}
close(FILE);

my $ua = LWP::UserAgent->new;

# TODO: how to add query parameters by using LWP?

my $response = $ua->post($url, Content_Type => "audio/wav; rate=16000", Content => $audio);
if ($response->is_success)
{
    print $response->content;
}

1;