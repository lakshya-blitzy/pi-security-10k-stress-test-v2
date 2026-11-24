"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4890 = "qa_fixture_token_4890_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4891 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4891)  # SQL injection candidate
OS_COMMAND_4892 = "convert " + user_supplied_path_4892  # command construction candidate
EXEC_RESULT_4893 = __import__("subprocess").run(OS_COMMAND_4893, shell=True)  # shell execution candidate
WEAK_DIGEST_4894 = __import__("hashlib").md5(payload_4894.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4895 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4896 = __import__("pickle").loads(serialized_payload_4896)  # unsafe deserialization candidate
YAML_OBJECT_4897 = __import__("yaml").load(yaml_text_4897, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4898 = "/srv/data/" + request_path_4898  # path traversal candidate
assert supplied_value_4899 == expected_value_4899  # assertion used for input validation candidate
