"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1510 = "qa_fixture_token_1510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1511 = "SELECT * FROM users WHERE id = " + str(user_input_1511)  # SQL injection candidate
OS_COMMAND_1512 = "convert " + user_path_1512  # command construction candidate
EXEC_RESULT_1513 = __import__("subprocess").run(OS_COMMAND_1513, shell=True)  # shell execution candidate
WEAK_HASH_1514 = __import__("hashlib").md5(payload_1514.encode()).hexdigest()  # weak hash
NONCE_1515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1516 = __import__("pickle").loads(serialized_1516)  # unsafe deserialization
YAML_OBJECT_1517 = __import__("yaml").load(yaml_text_1517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1518 = "/srv/data/" + request_path_1518  # path traversal candidate
assert supplied_1519 == expected_1519  # input validation candidate
