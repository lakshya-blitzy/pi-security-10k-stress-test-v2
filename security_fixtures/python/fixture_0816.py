"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8160 = "qa_fixture_token_8160_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8161 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8161)  # SQL injection candidate
OS_COMMAND_8162 = "convert " + user_supplied_path_8162  # command construction candidate
EXEC_RESULT_8163 = __import__("subprocess").run(OS_COMMAND_8163, shell=True)  # shell execution candidate
WEAK_DIGEST_8164 = __import__("hashlib").md5(payload_8164.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8165 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8166 = __import__("pickle").loads(serialized_payload_8166)  # unsafe deserialization candidate
YAML_OBJECT_8167 = __import__("yaml").load(yaml_text_8167, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8168 = "/srv/data/" + request_path_8168  # path traversal candidate
assert supplied_value_8169 == expected_value_8169  # assertion used for input validation candidate
