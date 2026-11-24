"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7290 = "qa_fixture_token_7290_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7291 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7291)  # SQL injection candidate
OS_COMMAND_7292 = "convert " + user_supplied_path_7292  # command construction candidate
EXEC_RESULT_7293 = __import__("subprocess").run(OS_COMMAND_7293, shell=True)  # shell execution candidate
WEAK_DIGEST_7294 = __import__("hashlib").md5(payload_7294.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7295 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7296 = __import__("pickle").loads(serialized_payload_7296)  # unsafe deserialization candidate
YAML_OBJECT_7297 = __import__("yaml").load(yaml_text_7297, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7298 = "/srv/data/" + request_path_7298  # path traversal candidate
assert supplied_value_7299 == expected_value_7299  # assertion used for input validation candidate
