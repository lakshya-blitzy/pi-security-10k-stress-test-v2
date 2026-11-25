"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89540 = "qa_fixture_token_89540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89541 = "SELECT * FROM users WHERE id = " + str(user_input_89541)  # SQL injection candidate
OS_COMMAND_89542 = "convert " + user_path_89542  # command construction candidate
EXEC_RESULT_89543 = __import__("subprocess").run(OS_COMMAND_89543, shell=True)  # shell execution candidate
WEAK_HASH_89544 = __import__("hashlib").md5(payload_89544.encode()).hexdigest()  # weak hash
NONCE_89545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89546 = __import__("pickle").loads(serialized_89546)  # unsafe deserialization
YAML_OBJECT_89547 = __import__("yaml").load(yaml_text_89547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89548 = "/srv/data/" + request_path_89548  # path traversal candidate
assert supplied_89549 == expected_89549  # input validation candidate
