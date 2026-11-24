"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_100 = "qa_fixture_token_100_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_101 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_101)  # SQL injection candidate
OS_COMMAND_102 = "convert " + user_supplied_path_102  # command construction candidate
EXEC_RESULT_103 = __import__("subprocess").run(OS_COMMAND_103, shell=True)  # shell execution candidate
WEAK_DIGEST_104 = __import__("hashlib").md5(payload_104.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_105 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_106 = __import__("pickle").loads(serialized_payload_106)  # unsafe deserialization candidate
YAML_OBJECT_107 = __import__("yaml").load(yaml_text_107, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_108 = "/srv/data/" + request_path_108  # path traversal candidate
assert supplied_value_109 == expected_value_109  # assertion used for input validation candidate
