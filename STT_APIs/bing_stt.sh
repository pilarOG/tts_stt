

#!/bin/bash

subscriptionKey=$1
filename="sample_short.wav" # duracion maxima son 15000 ms
output_format="detailed"
language="es-ES"
locale="en-US"
recognition_mode="conversation"

token=$(curl --fail -X POST "https://api.cognitive.microsoft.com/sts/v1.0/issueToken" \
                -H "Content-type: application/x-www-form-urlencoded" -H "Content-Length: 0" \
                -H "Ocp-Apim-Subscription-Key: $subscriptionKey")

if [ -z $token ] ; then
  echo "Request to issue an auth token failed." && exit 1;
fi

request_url="https://speech.platform.bing.com/speech/recognition/$recognition_mode"
request_url+="/cognitiveservices/v1?language=$language"
request_url+="&format=$output_format"

curl -v -X POST $request_url -H "Transfer-Encoding: chunked" \
        -H "Content-type: audio/wav; codec=audio/pcm; samplerate=44100" \
        -H "Authorization: Bearer $token" --data-binary @$filename

echo ""
