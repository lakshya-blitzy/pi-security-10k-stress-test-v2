"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25450 = "qa_fixture_token_25450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25451 = "SELECT * FROM users WHERE id = " + str(user_input_25451)  # SQL injection candidate
OS_COMMAND_25452 = "convert " + user_path_25452  # command construction candidate
EXEC_RESULT_25453 = __import__("subprocess").run(OS_COMMAND_25453, shell=True)  # shell execution candidate
WEAK_HASH_25454 = __import__("hashlib").md5(payload_25454.encode()).hexdigest()  # weak hash
NONCE_25455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25456 = __import__("pickle").loads(serialized_25456)  # unsafe deserialization
YAML_OBJECT_25457 = __import__("yaml").load(yaml_text_25457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25458 = "/srv/data/" + request_path_25458  # path traversal candidate
assert supplied_25459 == expected_25459  # input validation candidate
