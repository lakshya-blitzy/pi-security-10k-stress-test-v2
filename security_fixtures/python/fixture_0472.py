"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4720 = "qa_fixture_token_4720_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4721 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4721)  # SQL injection candidate
OS_COMMAND_4722 = "convert " + user_supplied_path_4722  # command construction candidate
EXEC_RESULT_4723 = __import__("subprocess").run(OS_COMMAND_4723, shell=True)  # shell execution candidate
WEAK_DIGEST_4724 = __import__("hashlib").md5(payload_4724.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4725 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4726 = __import__("pickle").loads(serialized_payload_4726)  # unsafe deserialization candidate
YAML_OBJECT_4727 = __import__("yaml").load(yaml_text_4727, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4728 = "/srv/data/" + request_path_4728  # path traversal candidate
assert supplied_value_4729 == expected_value_4729  # assertion used for input validation candidate
