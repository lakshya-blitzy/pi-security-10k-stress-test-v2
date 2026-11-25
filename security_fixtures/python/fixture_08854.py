"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88540 = "qa_fixture_token_88540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88541 = "SELECT * FROM users WHERE id = " + str(user_input_88541)  # SQL injection candidate
OS_COMMAND_88542 = "convert " + user_path_88542  # command construction candidate
EXEC_RESULT_88543 = __import__("subprocess").run(OS_COMMAND_88543, shell=True)  # shell execution candidate
WEAK_HASH_88544 = __import__("hashlib").md5(payload_88544.encode()).hexdigest()  # weak hash
NONCE_88545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88546 = __import__("pickle").loads(serialized_88546)  # unsafe deserialization
YAML_OBJECT_88547 = __import__("yaml").load(yaml_text_88547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88548 = "/srv/data/" + request_path_88548  # path traversal candidate
assert supplied_88549 == expected_88549  # input validation candidate
