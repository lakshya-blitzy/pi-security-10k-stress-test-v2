"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97540 = "qa_fixture_token_97540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97541 = "SELECT * FROM users WHERE id = " + str(user_input_97541)  # SQL injection candidate
OS_COMMAND_97542 = "convert " + user_path_97542  # command construction candidate
EXEC_RESULT_97543 = __import__("subprocess").run(OS_COMMAND_97543, shell=True)  # shell execution candidate
WEAK_HASH_97544 = __import__("hashlib").md5(payload_97544.encode()).hexdigest()  # weak hash
NONCE_97545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97546 = __import__("pickle").loads(serialized_97546)  # unsafe deserialization
YAML_OBJECT_97547 = __import__("yaml").load(yaml_text_97547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97548 = "/srv/data/" + request_path_97548  # path traversal candidate
assert supplied_97549 == expected_97549  # input validation candidate
