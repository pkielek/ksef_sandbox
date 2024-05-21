package com.github.ksef4dev;

import io.alapierre.ksef.client.AbstractApiClient;
import io.alapierre.ksef.client.ApiClient;
import io.alapierre.ksef.client.ApiException;
import io.alapierre.ksef.client.JsonSerializer;
import io.alapierre.ksef.client.api.InterfejsyInteraktywneSesjaApi;
import io.alapierre.ksef.client.model.rest.auth.AuthorisationChallengeResponse;
import io.alapierre.ksef.client.okhttp.OkHttpApiClient;
import io.alapierre.ksef.client.serializer.gson.GsonJsonSerializer;
import io.alapierre.ksef.token.facade.PublicKeyEncoder;
import lombok.val;

import java.text.ParseException;

import static io.alapierre.ksef.client.AbstractApiClient.Environment.TEST;
import static io.alapierre.ksef.client.model.rest.auth.AuthorisationChallengeRequest.IdentifierType.onip;

/**
 * @author Adrian Lapierre {@literal al@alapierre.io}
 * Copyrights by original author 2023.09.15
 */
public class EncryptAuthorizationToken {

    private static final JsonSerializer serializer = new GsonJsonSerializer();
    private static final ApiClient client = new OkHttpApiClient(serializer);
    private static final InterfejsyInteraktywneSesjaApi sesjaApi = new InterfejsyInteraktywneSesjaApi(client);

    public static void main(String[] args) throws ParseException, ApiException {

        if(args.length < 2) {
            System.out.println("Wymagane parametry wiersza poleceń NIP i token_autoryzacyjny");
            System.exit(1);
        }

        val identifier = args[0];
        val authorizationToken = args[1];

        val env = args.length == 3 ? AbstractApiClient.Environment.valueOf(args[2]) : TEST;

        AuthorisationChallengeResponse challengeResponse = sesjaApi.authorisationChallengeCall(identifier, onip);
        val timestamp = PublicKeyEncoder.parseChallengeTimestamp(challengeResponse.getTimestamp());

        PublicKeyEncoder encoder = PublicKeyEncoder.withBundledKey(env.name());
        String encryptedToken = encoder.encodeSessionToken(authorizationToken, timestamp);

        System.out.printf("token: %s\nchallenge: %s\n", encryptedToken, challengeResponse.getChallenge());

    }

}
