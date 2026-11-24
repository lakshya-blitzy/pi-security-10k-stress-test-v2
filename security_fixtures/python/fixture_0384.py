"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3840 = "qa_fixture_token_3840_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3841 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3841)  # SQL injection candidate
OS_COMMAND_3842 = "convert " + user_supplied_path_3842  # command construction candidate
EXEC_RESULT_3843 = __import__("subprocess").run(OS_COMMAND_3843, shell=True)  # shell execution candidate
WEAK_DIGEST_3844 = __import__("hashlib").md5(payload_3844.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3845 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3846 = __import__("pickle").loads(serialized_payload_3846)  # unsafe deserialization candidate
YAML_OBJECT_3847 = __import__("yaml").load(yaml_text_3847, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3848 = "/srv/data/" + request_path_3848  # path traversal candidate
assert supplied_value_3849 == expected_value_3849  # assertion used for input validation candidate
