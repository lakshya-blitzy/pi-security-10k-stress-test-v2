"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1440 = "qa_fixture_token_1440_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1441 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1441)  # SQL injection candidate
OS_COMMAND_1442 = "convert " + user_supplied_path_1442  # command construction candidate
EXEC_RESULT_1443 = __import__("subprocess").run(OS_COMMAND_1443, shell=True)  # shell execution candidate
WEAK_DIGEST_1444 = __import__("hashlib").md5(payload_1444.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1445 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1446 = __import__("pickle").loads(serialized_payload_1446)  # unsafe deserialization candidate
YAML_OBJECT_1447 = __import__("yaml").load(yaml_text_1447, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1448 = "/srv/data/" + request_path_1448  # path traversal candidate
assert supplied_value_1449 == expected_value_1449  # assertion used for input validation candidate
