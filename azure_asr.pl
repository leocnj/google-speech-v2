#!/usr/bin/perl
#
# based on http://bit.ly/10b6jx9
#
# TODO: convert to a Python version using urllib2
#
# 4/23/2013  This un-offical API still works.
#
require LWP::UserAgent;

my $url = "https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en-US";
my $audio = "";

open(FILE, "<" . $ARGV[0]);
while(<FILE>)
{
    $audio .= $_;
}
close(FILE);

my $ua = LWP::UserAgent->new;

my $response = $ua->post($url, Content_Type => "audio/x-flac; rate=16000", Content => $audio);
if ($response->is_success)
{
    print $response->content;
}

1;