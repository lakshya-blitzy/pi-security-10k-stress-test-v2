"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8190 = "qa_fixture_token_8190_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8191 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8191)  # SQL injection candidate
OS_COMMAND_8192 = "convert " + user_supplied_path_8192  # command construction candidate
EXEC_RESULT_8193 = __import__("subprocess").run(OS_COMMAND_8193, shell=True)  # shell execution candidate
WEAK_DIGEST_8194 = __import__("hashlib").md5(payload_8194.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8195 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8196 = __import__("pickle").loads(serialized_payload_8196)  # unsafe deserialization candidate
YAML_OBJECT_8197 = __import__("yaml").load(yaml_text_8197, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8198 = "/srv/data/" + request_path_8198  # path traversal candidate
assert supplied_value_8199 == expected_value_8199  # assertion used for input validation candidate
