"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1440 = "qa_fixture_token_1440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1441 = "SELECT * FROM users WHERE id = " + str(user_input_1441)  # SQL injection candidate
OS_COMMAND_1442 = "convert " + user_path_1442  # command construction candidate
EXEC_RESULT_1443 = __import__("subprocess").run(OS_COMMAND_1443, shell=True)  # shell execution candidate
WEAK_HASH_1444 = __import__("hashlib").md5(payload_1444.encode()).hexdigest()  # weak hash
NONCE_1445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1446 = __import__("pickle").loads(serialized_1446)  # unsafe deserialization
YAML_OBJECT_1447 = __import__("yaml").load(yaml_text_1447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1448 = "/srv/data/" + request_path_1448  # path traversal candidate
assert supplied_1449 == expected_1449  # input validation candidate
