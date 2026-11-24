"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4420 = "qa_fixture_token_4420_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4421 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4421)  # SQL injection candidate
OS_COMMAND_4422 = "convert " + user_supplied_path_4422  # command construction candidate
EXEC_RESULT_4423 = __import__("subprocess").run(OS_COMMAND_4423, shell=True)  # shell execution candidate
WEAK_DIGEST_4424 = __import__("hashlib").md5(payload_4424.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4425 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4426 = __import__("pickle").loads(serialized_payload_4426)  # unsafe deserialization candidate
YAML_OBJECT_4427 = __import__("yaml").load(yaml_text_4427, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4428 = "/srv/data/" + request_path_4428  # path traversal candidate
assert supplied_value_4429 == expected_value_4429  # assertion used for input validation candidate
