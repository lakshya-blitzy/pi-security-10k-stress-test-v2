"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8950 = "qa_fixture_token_8950_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8951 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8951)  # SQL injection candidate
OS_COMMAND_8952 = "convert " + user_supplied_path_8952  # command construction candidate
EXEC_RESULT_8953 = __import__("subprocess").run(OS_COMMAND_8953, shell=True)  # shell execution candidate
WEAK_DIGEST_8954 = __import__("hashlib").md5(payload_8954.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8955 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8956 = __import__("pickle").loads(serialized_payload_8956)  # unsafe deserialization candidate
YAML_OBJECT_8957 = __import__("yaml").load(yaml_text_8957, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8958 = "/srv/data/" + request_path_8958  # path traversal candidate
assert supplied_value_8959 == expected_value_8959  # assertion used for input validation candidate
