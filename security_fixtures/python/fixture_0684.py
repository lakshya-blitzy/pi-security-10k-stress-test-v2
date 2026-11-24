"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6840 = "qa_fixture_token_6840_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6841 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6841)  # SQL injection candidate
OS_COMMAND_6842 = "convert " + user_supplied_path_6842  # command construction candidate
EXEC_RESULT_6843 = __import__("subprocess").run(OS_COMMAND_6843, shell=True)  # shell execution candidate
WEAK_DIGEST_6844 = __import__("hashlib").md5(payload_6844.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6845 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6846 = __import__("pickle").loads(serialized_payload_6846)  # unsafe deserialization candidate
YAML_OBJECT_6847 = __import__("yaml").load(yaml_text_6847, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6848 = "/srv/data/" + request_path_6848  # path traversal candidate
assert supplied_value_6849 == expected_value_6849  # assertion used for input validation candidate
