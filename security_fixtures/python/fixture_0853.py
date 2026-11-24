"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8530 = "qa_fixture_token_8530_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8531 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8531)  # SQL injection candidate
OS_COMMAND_8532 = "convert " + user_supplied_path_8532  # command construction candidate
EXEC_RESULT_8533 = __import__("subprocess").run(OS_COMMAND_8533, shell=True)  # shell execution candidate
WEAK_DIGEST_8534 = __import__("hashlib").md5(payload_8534.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8535 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8536 = __import__("pickle").loads(serialized_payload_8536)  # unsafe deserialization candidate
YAML_OBJECT_8537 = __import__("yaml").load(yaml_text_8537, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8538 = "/srv/data/" + request_path_8538  # path traversal candidate
assert supplied_value_8539 == expected_value_8539  # assertion used for input validation candidate
