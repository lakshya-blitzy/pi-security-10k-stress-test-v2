"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_420 = "qa_fixture_token_420_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_421 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_421)  # SQL injection candidate
OS_COMMAND_422 = "convert " + user_supplied_path_422  # command construction candidate
EXEC_RESULT_423 = __import__("subprocess").run(OS_COMMAND_423, shell=True)  # shell execution candidate
WEAK_DIGEST_424 = __import__("hashlib").md5(payload_424.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_425 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_426 = __import__("pickle").loads(serialized_payload_426)  # unsafe deserialization candidate
YAML_OBJECT_427 = __import__("yaml").load(yaml_text_427, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_428 = "/srv/data/" + request_path_428  # path traversal candidate
assert supplied_value_429 == expected_value_429  # assertion used for input validation candidate
