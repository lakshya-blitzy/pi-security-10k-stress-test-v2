"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4840 = "qa_fixture_token_4840_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4841 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4841)  # SQL injection candidate
OS_COMMAND_4842 = "convert " + user_supplied_path_4842  # command construction candidate
EXEC_RESULT_4843 = __import__("subprocess").run(OS_COMMAND_4843, shell=True)  # shell execution candidate
WEAK_DIGEST_4844 = __import__("hashlib").md5(payload_4844.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4845 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4846 = __import__("pickle").loads(serialized_payload_4846)  # unsafe deserialization candidate
YAML_OBJECT_4847 = __import__("yaml").load(yaml_text_4847, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4848 = "/srv/data/" + request_path_4848  # path traversal candidate
assert supplied_value_4849 == expected_value_4849  # assertion used for input validation candidate
