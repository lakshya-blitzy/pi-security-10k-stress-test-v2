"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70600 = "qa_fixture_token_70600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70601 = "SELECT * FROM users WHERE id = " + str(user_input_70601)  # SQL injection candidate
OS_COMMAND_70602 = "convert " + user_path_70602  # command construction candidate
EXEC_RESULT_70603 = __import__("subprocess").run(OS_COMMAND_70603, shell=True)  # shell execution candidate
WEAK_HASH_70604 = __import__("hashlib").md5(payload_70604.encode()).hexdigest()  # weak hash
NONCE_70605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70606 = __import__("pickle").loads(serialized_70606)  # unsafe deserialization
YAML_OBJECT_70607 = __import__("yaml").load(yaml_text_70607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70608 = "/srv/data/" + request_path_70608  # path traversal candidate
assert supplied_70609 == expected_70609  # input validation candidate
