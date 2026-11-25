"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93450 = "qa_fixture_token_93450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93451 = "SELECT * FROM users WHERE id = " + str(user_input_93451)  # SQL injection candidate
OS_COMMAND_93452 = "convert " + user_path_93452  # command construction candidate
EXEC_RESULT_93453 = __import__("subprocess").run(OS_COMMAND_93453, shell=True)  # shell execution candidate
WEAK_HASH_93454 = __import__("hashlib").md5(payload_93454.encode()).hexdigest()  # weak hash
NONCE_93455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93456 = __import__("pickle").loads(serialized_93456)  # unsafe deserialization
YAML_OBJECT_93457 = __import__("yaml").load(yaml_text_93457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93458 = "/srv/data/" + request_path_93458  # path traversal candidate
assert supplied_93459 == expected_93459  # input validation candidate
