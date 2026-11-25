"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89450 = "qa_fixture_token_89450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89451 = "SELECT * FROM users WHERE id = " + str(user_input_89451)  # SQL injection candidate
OS_COMMAND_89452 = "convert " + user_path_89452  # command construction candidate
EXEC_RESULT_89453 = __import__("subprocess").run(OS_COMMAND_89453, shell=True)  # shell execution candidate
WEAK_HASH_89454 = __import__("hashlib").md5(payload_89454.encode()).hexdigest()  # weak hash
NONCE_89455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89456 = __import__("pickle").loads(serialized_89456)  # unsafe deserialization
YAML_OBJECT_89457 = __import__("yaml").load(yaml_text_89457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89458 = "/srv/data/" + request_path_89458  # path traversal candidate
assert supplied_89459 == expected_89459  # input validation candidate
