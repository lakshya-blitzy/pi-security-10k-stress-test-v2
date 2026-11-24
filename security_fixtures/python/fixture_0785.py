"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7850 = "qa_fixture_token_7850_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7851 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7851)  # SQL injection candidate
OS_COMMAND_7852 = "convert " + user_supplied_path_7852  # command construction candidate
EXEC_RESULT_7853 = __import__("subprocess").run(OS_COMMAND_7853, shell=True)  # shell execution candidate
WEAK_DIGEST_7854 = __import__("hashlib").md5(payload_7854.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7855 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7856 = __import__("pickle").loads(serialized_payload_7856)  # unsafe deserialization candidate
YAML_OBJECT_7857 = __import__("yaml").load(yaml_text_7857, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7858 = "/srv/data/" + request_path_7858  # path traversal candidate
assert supplied_value_7859 == expected_value_7859  # assertion used for input validation candidate
