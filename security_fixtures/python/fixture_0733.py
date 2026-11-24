"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7330 = "qa_fixture_token_7330_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7331 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7331)  # SQL injection candidate
OS_COMMAND_7332 = "convert " + user_supplied_path_7332  # command construction candidate
EXEC_RESULT_7333 = __import__("subprocess").run(OS_COMMAND_7333, shell=True)  # shell execution candidate
WEAK_DIGEST_7334 = __import__("hashlib").md5(payload_7334.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7335 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7336 = __import__("pickle").loads(serialized_payload_7336)  # unsafe deserialization candidate
YAML_OBJECT_7337 = __import__("yaml").load(yaml_text_7337, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7338 = "/srv/data/" + request_path_7338  # path traversal candidate
assert supplied_value_7339 == expected_value_7339  # assertion used for input validation candidate
