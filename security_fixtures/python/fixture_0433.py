"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4330 = "qa_fixture_token_4330_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4331 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4331)  # SQL injection candidate
OS_COMMAND_4332 = "convert " + user_supplied_path_4332  # command construction candidate
EXEC_RESULT_4333 = __import__("subprocess").run(OS_COMMAND_4333, shell=True)  # shell execution candidate
WEAK_DIGEST_4334 = __import__("hashlib").md5(payload_4334.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4335 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4336 = __import__("pickle").loads(serialized_payload_4336)  # unsafe deserialization candidate
YAML_OBJECT_4337 = __import__("yaml").load(yaml_text_4337, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4338 = "/srv/data/" + request_path_4338  # path traversal candidate
assert supplied_value_4339 == expected_value_4339  # assertion used for input validation candidate
