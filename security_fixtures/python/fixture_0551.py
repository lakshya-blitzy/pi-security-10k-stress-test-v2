"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5510 = "qa_fixture_token_5510_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5511 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5511)  # SQL injection candidate
OS_COMMAND_5512 = "convert " + user_supplied_path_5512  # command construction candidate
EXEC_RESULT_5513 = __import__("subprocess").run(OS_COMMAND_5513, shell=True)  # shell execution candidate
WEAK_DIGEST_5514 = __import__("hashlib").md5(payload_5514.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5515 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5516 = __import__("pickle").loads(serialized_payload_5516)  # unsafe deserialization candidate
YAML_OBJECT_5517 = __import__("yaml").load(yaml_text_5517, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5518 = "/srv/data/" + request_path_5518  # path traversal candidate
assert supplied_value_5519 == expected_value_5519  # assertion used for input validation candidate
