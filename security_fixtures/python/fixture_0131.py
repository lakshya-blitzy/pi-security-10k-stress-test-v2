"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1310 = "qa_fixture_token_1310_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1311 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1311)  # SQL injection candidate
OS_COMMAND_1312 = "convert " + user_supplied_path_1312  # command construction candidate
EXEC_RESULT_1313 = __import__("subprocess").run(OS_COMMAND_1313, shell=True)  # shell execution candidate
WEAK_DIGEST_1314 = __import__("hashlib").md5(payload_1314.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1315 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1316 = __import__("pickle").loads(serialized_payload_1316)  # unsafe deserialization candidate
YAML_OBJECT_1317 = __import__("yaml").load(yaml_text_1317, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1318 = "/srv/data/" + request_path_1318  # path traversal candidate
assert supplied_value_1319 == expected_value_1319  # assertion used for input validation candidate
