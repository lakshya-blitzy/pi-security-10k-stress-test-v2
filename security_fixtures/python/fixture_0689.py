"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6890 = "qa_fixture_token_6890_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6891 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6891)  # SQL injection candidate
OS_COMMAND_6892 = "convert " + user_supplied_path_6892  # command construction candidate
EXEC_RESULT_6893 = __import__("subprocess").run(OS_COMMAND_6893, shell=True)  # shell execution candidate
WEAK_DIGEST_6894 = __import__("hashlib").md5(payload_6894.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6895 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6896 = __import__("pickle").loads(serialized_payload_6896)  # unsafe deserialization candidate
YAML_OBJECT_6897 = __import__("yaml").load(yaml_text_6897, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6898 = "/srv/data/" + request_path_6898  # path traversal candidate
assert supplied_value_6899 == expected_value_6899  # assertion used for input validation candidate
