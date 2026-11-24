"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7190 = "qa_fixture_token_7190_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7191 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7191)  # SQL injection candidate
OS_COMMAND_7192 = "convert " + user_supplied_path_7192  # command construction candidate
EXEC_RESULT_7193 = __import__("subprocess").run(OS_COMMAND_7193, shell=True)  # shell execution candidate
WEAK_DIGEST_7194 = __import__("hashlib").md5(payload_7194.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7195 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7196 = __import__("pickle").loads(serialized_payload_7196)  # unsafe deserialization candidate
YAML_OBJECT_7197 = __import__("yaml").load(yaml_text_7197, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7198 = "/srv/data/" + request_path_7198  # path traversal candidate
assert supplied_value_7199 == expected_value_7199  # assertion used for input validation candidate
