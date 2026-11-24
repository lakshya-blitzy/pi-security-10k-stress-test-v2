"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1470 = "qa_fixture_token_1470_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1471 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1471)  # SQL injection candidate
OS_COMMAND_1472 = "convert " + user_supplied_path_1472  # command construction candidate
EXEC_RESULT_1473 = __import__("subprocess").run(OS_COMMAND_1473, shell=True)  # shell execution candidate
WEAK_DIGEST_1474 = __import__("hashlib").md5(payload_1474.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1475 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1476 = __import__("pickle").loads(serialized_payload_1476)  # unsafe deserialization candidate
YAML_OBJECT_1477 = __import__("yaml").load(yaml_text_1477, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1478 = "/srv/data/" + request_path_1478  # path traversal candidate
assert supplied_value_1479 == expected_value_1479  # assertion used for input validation candidate
