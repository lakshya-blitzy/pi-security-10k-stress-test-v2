"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1490 = "qa_fixture_token_1490_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1491 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1491)  # SQL injection candidate
OS_COMMAND_1492 = "convert " + user_supplied_path_1492  # command construction candidate
EXEC_RESULT_1493 = __import__("subprocess").run(OS_COMMAND_1493, shell=True)  # shell execution candidate
WEAK_DIGEST_1494 = __import__("hashlib").md5(payload_1494.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1495 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1496 = __import__("pickle").loads(serialized_payload_1496)  # unsafe deserialization candidate
YAML_OBJECT_1497 = __import__("yaml").load(yaml_text_1497, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1498 = "/srv/data/" + request_path_1498  # path traversal candidate
assert supplied_value_1499 == expected_value_1499  # assertion used for input validation candidate
