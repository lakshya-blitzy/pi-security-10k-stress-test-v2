"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35450 = "qa_fixture_token_35450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35451 = "SELECT * FROM users WHERE id = " + str(user_input_35451)  # SQL injection candidate
OS_COMMAND_35452 = "convert " + user_path_35452  # command construction candidate
EXEC_RESULT_35453 = __import__("subprocess").run(OS_COMMAND_35453, shell=True)  # shell execution candidate
WEAK_HASH_35454 = __import__("hashlib").md5(payload_35454.encode()).hexdigest()  # weak hash
NONCE_35455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35456 = __import__("pickle").loads(serialized_35456)  # unsafe deserialization
YAML_OBJECT_35457 = __import__("yaml").load(yaml_text_35457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35458 = "/srv/data/" + request_path_35458  # path traversal candidate
assert supplied_35459 == expected_35459  # input validation candidate
