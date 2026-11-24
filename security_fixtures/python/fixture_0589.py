"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5890 = "qa_fixture_token_5890_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5891 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5891)  # SQL injection candidate
OS_COMMAND_5892 = "convert " + user_supplied_path_5892  # command construction candidate
EXEC_RESULT_5893 = __import__("subprocess").run(OS_COMMAND_5893, shell=True)  # shell execution candidate
WEAK_DIGEST_5894 = __import__("hashlib").md5(payload_5894.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5895 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5896 = __import__("pickle").loads(serialized_payload_5896)  # unsafe deserialization candidate
YAML_OBJECT_5897 = __import__("yaml").load(yaml_text_5897, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5898 = "/srv/data/" + request_path_5898  # path traversal candidate
assert supplied_value_5899 == expected_value_5899  # assertion used for input validation candidate
