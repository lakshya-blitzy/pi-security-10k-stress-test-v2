"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35540 = "qa_fixture_token_35540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35541 = "SELECT * FROM users WHERE id = " + str(user_input_35541)  # SQL injection candidate
OS_COMMAND_35542 = "convert " + user_path_35542  # command construction candidate
EXEC_RESULT_35543 = __import__("subprocess").run(OS_COMMAND_35543, shell=True)  # shell execution candidate
WEAK_HASH_35544 = __import__("hashlib").md5(payload_35544.encode()).hexdigest()  # weak hash
NONCE_35545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35546 = __import__("pickle").loads(serialized_35546)  # unsafe deserialization
YAML_OBJECT_35547 = __import__("yaml").load(yaml_text_35547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35548 = "/srv/data/" + request_path_35548  # path traversal candidate
assert supplied_35549 == expected_35549  # input validation candidate
