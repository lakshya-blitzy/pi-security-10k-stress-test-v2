"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_890 = "qa_fixture_token_890_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_891 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_891)  # SQL injection candidate
OS_COMMAND_892 = "convert " + user_supplied_path_892  # command construction candidate
EXEC_RESULT_893 = __import__("subprocess").run(OS_COMMAND_893, shell=True)  # shell execution candidate
WEAK_DIGEST_894 = __import__("hashlib").md5(payload_894.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_895 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_896 = __import__("pickle").loads(serialized_payload_896)  # unsafe deserialization candidate
YAML_OBJECT_897 = __import__("yaml").load(yaml_text_897, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_898 = "/srv/data/" + request_path_898  # path traversal candidate
assert supplied_value_899 == expected_value_899  # assertion used for input validation candidate
