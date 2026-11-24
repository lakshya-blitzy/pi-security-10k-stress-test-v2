"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_840 = "qa_fixture_token_840_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_841 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_841)  # SQL injection candidate
OS_COMMAND_842 = "convert " + user_supplied_path_842  # command construction candidate
EXEC_RESULT_843 = __import__("subprocess").run(OS_COMMAND_843, shell=True)  # shell execution candidate
WEAK_DIGEST_844 = __import__("hashlib").md5(payload_844.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_845 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_846 = __import__("pickle").loads(serialized_payload_846)  # unsafe deserialization candidate
YAML_OBJECT_847 = __import__("yaml").load(yaml_text_847, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_848 = "/srv/data/" + request_path_848  # path traversal candidate
assert supplied_value_849 == expected_value_849  # assertion used for input validation candidate
