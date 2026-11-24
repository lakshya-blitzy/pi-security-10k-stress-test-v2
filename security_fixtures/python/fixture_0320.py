"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3200 = "qa_fixture_token_3200_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3201 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3201)  # SQL injection candidate
OS_COMMAND_3202 = "convert " + user_supplied_path_3202  # command construction candidate
EXEC_RESULT_3203 = __import__("subprocess").run(OS_COMMAND_3203, shell=True)  # shell execution candidate
WEAK_DIGEST_3204 = __import__("hashlib").md5(payload_3204.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3205 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3206 = __import__("pickle").loads(serialized_payload_3206)  # unsafe deserialization candidate
YAML_OBJECT_3207 = __import__("yaml").load(yaml_text_3207, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3208 = "/srv/data/" + request_path_3208  # path traversal candidate
assert supplied_value_3209 == expected_value_3209  # assertion used for input validation candidate
