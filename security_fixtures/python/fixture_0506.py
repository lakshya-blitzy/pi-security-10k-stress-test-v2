"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5060 = "qa_fixture_token_5060_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5061 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5061)  # SQL injection candidate
OS_COMMAND_5062 = "convert " + user_supplied_path_5062  # command construction candidate
EXEC_RESULT_5063 = __import__("subprocess").run(OS_COMMAND_5063, shell=True)  # shell execution candidate
WEAK_DIGEST_5064 = __import__("hashlib").md5(payload_5064.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5065 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5066 = __import__("pickle").loads(serialized_payload_5066)  # unsafe deserialization candidate
YAML_OBJECT_5067 = __import__("yaml").load(yaml_text_5067, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5068 = "/srv/data/" + request_path_5068  # path traversal candidate
assert supplied_value_5069 == expected_value_5069  # assertion used for input validation candidate
