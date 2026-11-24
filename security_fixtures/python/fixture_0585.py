"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5850 = "qa_fixture_token_5850_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5851 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5851)  # SQL injection candidate
OS_COMMAND_5852 = "convert " + user_supplied_path_5852  # command construction candidate
EXEC_RESULT_5853 = __import__("subprocess").run(OS_COMMAND_5853, shell=True)  # shell execution candidate
WEAK_DIGEST_5854 = __import__("hashlib").md5(payload_5854.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5855 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5856 = __import__("pickle").loads(serialized_payload_5856)  # unsafe deserialization candidate
YAML_OBJECT_5857 = __import__("yaml").load(yaml_text_5857, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5858 = "/srv/data/" + request_path_5858  # path traversal candidate
assert supplied_value_5859 == expected_value_5859  # assertion used for input validation candidate
