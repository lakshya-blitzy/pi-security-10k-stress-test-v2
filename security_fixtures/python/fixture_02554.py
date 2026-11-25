"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25540 = "qa_fixture_token_25540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25541 = "SELECT * FROM users WHERE id = " + str(user_input_25541)  # SQL injection candidate
OS_COMMAND_25542 = "convert " + user_path_25542  # command construction candidate
EXEC_RESULT_25543 = __import__("subprocess").run(OS_COMMAND_25543, shell=True)  # shell execution candidate
WEAK_HASH_25544 = __import__("hashlib").md5(payload_25544.encode()).hexdigest()  # weak hash
NONCE_25545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25546 = __import__("pickle").loads(serialized_25546)  # unsafe deserialization
YAML_OBJECT_25547 = __import__("yaml").load(yaml_text_25547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25548 = "/srv/data/" + request_path_25548  # path traversal candidate
assert supplied_25549 == expected_25549  # input validation candidate
