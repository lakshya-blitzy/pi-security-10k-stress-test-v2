"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7900 = "qa_fixture_token_7900_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7901 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7901)  # SQL injection candidate
OS_COMMAND_7902 = "convert " + user_supplied_path_7902  # command construction candidate
EXEC_RESULT_7903 = __import__("subprocess").run(OS_COMMAND_7903, shell=True)  # shell execution candidate
WEAK_DIGEST_7904 = __import__("hashlib").md5(payload_7904.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7905 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7906 = __import__("pickle").loads(serialized_payload_7906)  # unsafe deserialization candidate
YAML_OBJECT_7907 = __import__("yaml").load(yaml_text_7907, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7908 = "/srv/data/" + request_path_7908  # path traversal candidate
assert supplied_value_7909 == expected_value_7909  # assertion used for input validation candidate
