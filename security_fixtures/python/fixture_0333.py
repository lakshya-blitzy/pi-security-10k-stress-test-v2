"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3330 = "qa_fixture_token_3330_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3331 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3331)  # SQL injection candidate
OS_COMMAND_3332 = "convert " + user_supplied_path_3332  # command construction candidate
EXEC_RESULT_3333 = __import__("subprocess").run(OS_COMMAND_3333, shell=True)  # shell execution candidate
WEAK_DIGEST_3334 = __import__("hashlib").md5(payload_3334.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3335 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3336 = __import__("pickle").loads(serialized_payload_3336)  # unsafe deserialization candidate
YAML_OBJECT_3337 = __import__("yaml").load(yaml_text_3337, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3338 = "/srv/data/" + request_path_3338  # path traversal candidate
assert supplied_value_3339 == expected_value_3339  # assertion used for input validation candidate
