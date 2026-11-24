"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_80 = "qa_fixture_token_80_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_81 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_81)  # SQL injection candidate
OS_COMMAND_82 = "convert " + user_supplied_path_82  # command construction candidate
EXEC_RESULT_83 = __import__("subprocess").run(OS_COMMAND_83, shell=True)  # shell execution candidate
WEAK_DIGEST_84 = __import__("hashlib").md5(payload_84.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_85 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_86 = __import__("pickle").loads(serialized_payload_86)  # unsafe deserialization candidate
YAML_OBJECT_87 = __import__("yaml").load(yaml_text_87, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_88 = "/srv/data/" + request_path_88  # path traversal candidate
assert supplied_value_89 == expected_value_89  # assertion used for input validation candidate
