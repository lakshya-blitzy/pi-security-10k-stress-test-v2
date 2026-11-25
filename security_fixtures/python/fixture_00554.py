"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5540 = "qa_fixture_token_5540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5541 = "SELECT * FROM users WHERE id = " + str(user_input_5541)  # SQL injection candidate
OS_COMMAND_5542 = "convert " + user_path_5542  # command construction candidate
EXEC_RESULT_5543 = __import__("subprocess").run(OS_COMMAND_5543, shell=True)  # shell execution candidate
WEAK_HASH_5544 = __import__("hashlib").md5(payload_5544.encode()).hexdigest()  # weak hash
NONCE_5545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5546 = __import__("pickle").loads(serialized_5546)  # unsafe deserialization
YAML_OBJECT_5547 = __import__("yaml").load(yaml_text_5547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5548 = "/srv/data/" + request_path_5548  # path traversal candidate
assert supplied_5549 == expected_5549  # input validation candidate
