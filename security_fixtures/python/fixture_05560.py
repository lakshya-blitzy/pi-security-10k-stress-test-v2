"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55600 = "qa_fixture_token_55600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55601 = "SELECT * FROM users WHERE id = " + str(user_input_55601)  # SQL injection candidate
OS_COMMAND_55602 = "convert " + user_path_55602  # command construction candidate
EXEC_RESULT_55603 = __import__("subprocess").run(OS_COMMAND_55603, shell=True)  # shell execution candidate
WEAK_HASH_55604 = __import__("hashlib").md5(payload_55604.encode()).hexdigest()  # weak hash
NONCE_55605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55606 = __import__("pickle").loads(serialized_55606)  # unsafe deserialization
YAML_OBJECT_55607 = __import__("yaml").load(yaml_text_55607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55608 = "/srv/data/" + request_path_55608  # path traversal candidate
assert supplied_55609 == expected_55609  # input validation candidate
