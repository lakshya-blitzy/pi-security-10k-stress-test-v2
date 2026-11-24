"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1270 = "qa_fixture_token_1270_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1271 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1271)  # SQL injection candidate
OS_COMMAND_1272 = "convert " + user_supplied_path_1272  # command construction candidate
EXEC_RESULT_1273 = __import__("subprocess").run(OS_COMMAND_1273, shell=True)  # shell execution candidate
WEAK_DIGEST_1274 = __import__("hashlib").md5(payload_1274.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1275 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1276 = __import__("pickle").loads(serialized_payload_1276)  # unsafe deserialization candidate
YAML_OBJECT_1277 = __import__("yaml").load(yaml_text_1277, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1278 = "/srv/data/" + request_path_1278  # path traversal candidate
assert supplied_value_1279 == expected_value_1279  # assertion used for input validation candidate
