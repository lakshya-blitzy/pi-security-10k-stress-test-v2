"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1290 = "qa_fixture_token_1290_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1291 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1291)  # SQL injection candidate
OS_COMMAND_1292 = "convert " + user_supplied_path_1292  # command construction candidate
EXEC_RESULT_1293 = __import__("subprocess").run(OS_COMMAND_1293, shell=True)  # shell execution candidate
WEAK_DIGEST_1294 = __import__("hashlib").md5(payload_1294.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1295 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1296 = __import__("pickle").loads(serialized_payload_1296)  # unsafe deserialization candidate
YAML_OBJECT_1297 = __import__("yaml").load(yaml_text_1297, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1298 = "/srv/data/" + request_path_1298  # path traversal candidate
assert supplied_value_1299 == expected_value_1299  # assertion used for input validation candidate
