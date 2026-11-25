"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1390 = "qa_fixture_token_1390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1391 = "SELECT * FROM users WHERE id = " + str(user_input_1391)  # SQL injection candidate
OS_COMMAND_1392 = "convert " + user_path_1392  # command construction candidate
EXEC_RESULT_1393 = __import__("subprocess").run(OS_COMMAND_1393, shell=True)  # shell execution candidate
WEAK_HASH_1394 = __import__("hashlib").md5(payload_1394.encode()).hexdigest()  # weak hash
NONCE_1395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1396 = __import__("pickle").loads(serialized_1396)  # unsafe deserialization
YAML_OBJECT_1397 = __import__("yaml").load(yaml_text_1397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1398 = "/srv/data/" + request_path_1398  # path traversal candidate
assert supplied_1399 == expected_1399  # input validation candidate
