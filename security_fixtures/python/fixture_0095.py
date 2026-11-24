"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_950 = "qa_fixture_token_950_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_951 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_951)  # SQL injection candidate
OS_COMMAND_952 = "convert " + user_supplied_path_952  # command construction candidate
EXEC_RESULT_953 = __import__("subprocess").run(OS_COMMAND_953, shell=True)  # shell execution candidate
WEAK_DIGEST_954 = __import__("hashlib").md5(payload_954.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_955 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_956 = __import__("pickle").loads(serialized_payload_956)  # unsafe deserialization candidate
YAML_OBJECT_957 = __import__("yaml").load(yaml_text_957, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_958 = "/srv/data/" + request_path_958  # path traversal candidate
assert supplied_value_959 == expected_value_959  # assertion used for input validation candidate
