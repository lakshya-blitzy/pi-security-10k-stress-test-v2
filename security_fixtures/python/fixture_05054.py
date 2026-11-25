"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50540 = "qa_fixture_token_50540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50541 = "SELECT * FROM users WHERE id = " + str(user_input_50541)  # SQL injection candidate
OS_COMMAND_50542 = "convert " + user_path_50542  # command construction candidate
EXEC_RESULT_50543 = __import__("subprocess").run(OS_COMMAND_50543, shell=True)  # shell execution candidate
WEAK_HASH_50544 = __import__("hashlib").md5(payload_50544.encode()).hexdigest()  # weak hash
NONCE_50545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50546 = __import__("pickle").loads(serialized_50546)  # unsafe deserialization
YAML_OBJECT_50547 = __import__("yaml").load(yaml_text_50547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50548 = "/srv/data/" + request_path_50548  # path traversal candidate
assert supplied_50549 == expected_50549  # input validation candidate
