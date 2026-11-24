"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5330 = "qa_fixture_token_5330_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5331 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5331)  # SQL injection candidate
OS_COMMAND_5332 = "convert " + user_supplied_path_5332  # command construction candidate
EXEC_RESULT_5333 = __import__("subprocess").run(OS_COMMAND_5333, shell=True)  # shell execution candidate
WEAK_DIGEST_5334 = __import__("hashlib").md5(payload_5334.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5335 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5336 = __import__("pickle").loads(serialized_payload_5336)  # unsafe deserialization candidate
YAML_OBJECT_5337 = __import__("yaml").load(yaml_text_5337, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5338 = "/srv/data/" + request_path_5338  # path traversal candidate
assert supplied_value_5339 == expected_value_5339  # assertion used for input validation candidate
