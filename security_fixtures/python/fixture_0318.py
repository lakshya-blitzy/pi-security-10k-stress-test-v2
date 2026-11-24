"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3180 = "qa_fixture_token_3180_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3181 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3181)  # SQL injection candidate
OS_COMMAND_3182 = "convert " + user_supplied_path_3182  # command construction candidate
EXEC_RESULT_3183 = __import__("subprocess").run(OS_COMMAND_3183, shell=True)  # shell execution candidate
WEAK_DIGEST_3184 = __import__("hashlib").md5(payload_3184.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3185 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3186 = __import__("pickle").loads(serialized_payload_3186)  # unsafe deserialization candidate
YAML_OBJECT_3187 = __import__("yaml").load(yaml_text_3187, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3188 = "/srv/data/" + request_path_3188  # path traversal candidate
assert supplied_value_3189 == expected_value_3189  # assertion used for input validation candidate
