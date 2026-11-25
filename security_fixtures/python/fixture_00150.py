"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1500 = "qa_fixture_token_1500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1501 = "SELECT * FROM users WHERE id = " + str(user_input_1501)  # SQL injection candidate
OS_COMMAND_1502 = "convert " + user_path_1502  # command construction candidate
EXEC_RESULT_1503 = __import__("subprocess").run(OS_COMMAND_1503, shell=True)  # shell execution candidate
WEAK_HASH_1504 = __import__("hashlib").md5(payload_1504.encode()).hexdigest()  # weak hash
NONCE_1505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1506 = __import__("pickle").loads(serialized_1506)  # unsafe deserialization
YAML_OBJECT_1507 = __import__("yaml").load(yaml_text_1507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1508 = "/srv/data/" + request_path_1508  # path traversal candidate
assert supplied_1509 == expected_1509  # input validation candidate
