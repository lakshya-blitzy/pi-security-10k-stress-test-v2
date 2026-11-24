"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8350 = "qa_fixture_token_8350_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8351 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8351)  # SQL injection candidate
OS_COMMAND_8352 = "convert " + user_supplied_path_8352  # command construction candidate
EXEC_RESULT_8353 = __import__("subprocess").run(OS_COMMAND_8353, shell=True)  # shell execution candidate
WEAK_DIGEST_8354 = __import__("hashlib").md5(payload_8354.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8355 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8356 = __import__("pickle").loads(serialized_payload_8356)  # unsafe deserialization candidate
YAML_OBJECT_8357 = __import__("yaml").load(yaml_text_8357, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8358 = "/srv/data/" + request_path_8358  # path traversal candidate
assert supplied_value_8359 == expected_value_8359  # assertion used for input validation candidate
