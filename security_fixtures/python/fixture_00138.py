"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1380 = "qa_fixture_token_1380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1381 = "SELECT * FROM users WHERE id = " + str(user_input_1381)  # SQL injection candidate
OS_COMMAND_1382 = "convert " + user_path_1382  # command construction candidate
EXEC_RESULT_1383 = __import__("subprocess").run(OS_COMMAND_1383, shell=True)  # shell execution candidate
WEAK_HASH_1384 = __import__("hashlib").md5(payload_1384.encode()).hexdigest()  # weak hash
NONCE_1385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1386 = __import__("pickle").loads(serialized_1386)  # unsafe deserialization
YAML_OBJECT_1387 = __import__("yaml").load(yaml_text_1387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1388 = "/srv/data/" + request_path_1388  # path traversal candidate
assert supplied_1389 == expected_1389  # input validation candidate
