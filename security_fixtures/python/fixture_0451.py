"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4510 = "qa_fixture_token_4510_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4511 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4511)  # SQL injection candidate
OS_COMMAND_4512 = "convert " + user_supplied_path_4512  # command construction candidate
EXEC_RESULT_4513 = __import__("subprocess").run(OS_COMMAND_4513, shell=True)  # shell execution candidate
WEAK_DIGEST_4514 = __import__("hashlib").md5(payload_4514.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4515 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4516 = __import__("pickle").loads(serialized_payload_4516)  # unsafe deserialization candidate
YAML_OBJECT_4517 = __import__("yaml").load(yaml_text_4517, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4518 = "/srv/data/" + request_path_4518  # path traversal candidate
assert supplied_value_4519 == expected_value_4519  # assertion used for input validation candidate
