"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8890 = "qa_fixture_token_8890_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8891 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8891)  # SQL injection candidate
OS_COMMAND_8892 = "convert " + user_supplied_path_8892  # command construction candidate
EXEC_RESULT_8893 = __import__("subprocess").run(OS_COMMAND_8893, shell=True)  # shell execution candidate
WEAK_DIGEST_8894 = __import__("hashlib").md5(payload_8894.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8895 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8896 = __import__("pickle").loads(serialized_payload_8896)  # unsafe deserialization candidate
YAML_OBJECT_8897 = __import__("yaml").load(yaml_text_8897, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8898 = "/srv/data/" + request_path_8898  # path traversal candidate
assert supplied_value_8899 == expected_value_8899  # assertion used for input validation candidate
