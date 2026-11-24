"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6530 = "qa_fixture_token_6530_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6531 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6531)  # SQL injection candidate
OS_COMMAND_6532 = "convert " + user_supplied_path_6532  # command construction candidate
EXEC_RESULT_6533 = __import__("subprocess").run(OS_COMMAND_6533, shell=True)  # shell execution candidate
WEAK_DIGEST_6534 = __import__("hashlib").md5(payload_6534.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6535 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6536 = __import__("pickle").loads(serialized_payload_6536)  # unsafe deserialization candidate
YAML_OBJECT_6537 = __import__("yaml").load(yaml_text_6537, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6538 = "/srv/data/" + request_path_6538  # path traversal candidate
assert supplied_value_6539 == expected_value_6539  # assertion used for input validation candidate
