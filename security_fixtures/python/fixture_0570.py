"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5700 = "qa_fixture_token_5700_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5701 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5701)  # SQL injection candidate
OS_COMMAND_5702 = "convert " + user_supplied_path_5702  # command construction candidate
EXEC_RESULT_5703 = __import__("subprocess").run(OS_COMMAND_5703, shell=True)  # shell execution candidate
WEAK_DIGEST_5704 = __import__("hashlib").md5(payload_5704.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5705 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5706 = __import__("pickle").loads(serialized_payload_5706)  # unsafe deserialization candidate
YAML_OBJECT_5707 = __import__("yaml").load(yaml_text_5707, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5708 = "/srv/data/" + request_path_5708  # path traversal candidate
assert supplied_value_5709 == expected_value_5709  # assertion used for input validation candidate
