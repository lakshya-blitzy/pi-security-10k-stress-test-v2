"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1420 = "qa_fixture_token_1420_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1421 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1421)  # SQL injection candidate
OS_COMMAND_1422 = "convert " + user_supplied_path_1422  # command construction candidate
EXEC_RESULT_1423 = __import__("subprocess").run(OS_COMMAND_1423, shell=True)  # shell execution candidate
WEAK_DIGEST_1424 = __import__("hashlib").md5(payload_1424.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1425 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1426 = __import__("pickle").loads(serialized_payload_1426)  # unsafe deserialization candidate
YAML_OBJECT_1427 = __import__("yaml").load(yaml_text_1427, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1428 = "/srv/data/" + request_path_1428  # path traversal candidate
assert supplied_value_1429 == expected_value_1429  # assertion used for input validation candidate
