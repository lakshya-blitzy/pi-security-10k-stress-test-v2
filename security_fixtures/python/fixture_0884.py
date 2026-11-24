"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8840 = "qa_fixture_token_8840_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8841 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8841)  # SQL injection candidate
OS_COMMAND_8842 = "convert " + user_supplied_path_8842  # command construction candidate
EXEC_RESULT_8843 = __import__("subprocess").run(OS_COMMAND_8843, shell=True)  # shell execution candidate
WEAK_DIGEST_8844 = __import__("hashlib").md5(payload_8844.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8845 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8846 = __import__("pickle").loads(serialized_payload_8846)  # unsafe deserialization candidate
YAML_OBJECT_8847 = __import__("yaml").load(yaml_text_8847, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8848 = "/srv/data/" + request_path_8848  # path traversal candidate
assert supplied_value_8849 == expected_value_8849  # assertion used for input validation candidate
