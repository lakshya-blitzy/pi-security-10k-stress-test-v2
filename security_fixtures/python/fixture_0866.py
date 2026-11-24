"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8660 = "qa_fixture_token_8660_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8661 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8661)  # SQL injection candidate
OS_COMMAND_8662 = "convert " + user_supplied_path_8662  # command construction candidate
EXEC_RESULT_8663 = __import__("subprocess").run(OS_COMMAND_8663, shell=True)  # shell execution candidate
WEAK_DIGEST_8664 = __import__("hashlib").md5(payload_8664.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8665 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8666 = __import__("pickle").loads(serialized_payload_8666)  # unsafe deserialization candidate
YAML_OBJECT_8667 = __import__("yaml").load(yaml_text_8667, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8668 = "/srv/data/" + request_path_8668  # path traversal candidate
assert supplied_value_8669 == expected_value_8669  # assertion used for input validation candidate
