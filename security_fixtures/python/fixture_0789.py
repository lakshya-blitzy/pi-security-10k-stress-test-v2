"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7890 = "qa_fixture_token_7890_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7891 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7891)  # SQL injection candidate
OS_COMMAND_7892 = "convert " + user_supplied_path_7892  # command construction candidate
EXEC_RESULT_7893 = __import__("subprocess").run(OS_COMMAND_7893, shell=True)  # shell execution candidate
WEAK_DIGEST_7894 = __import__("hashlib").md5(payload_7894.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7895 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7896 = __import__("pickle").loads(serialized_payload_7896)  # unsafe deserialization candidate
YAML_OBJECT_7897 = __import__("yaml").load(yaml_text_7897, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7898 = "/srv/data/" + request_path_7898  # path traversal candidate
assert supplied_value_7899 == expected_value_7899  # assertion used for input validation candidate
