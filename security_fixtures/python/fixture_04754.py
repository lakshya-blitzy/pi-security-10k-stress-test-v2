"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47540 = "qa_fixture_token_47540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47541 = "SELECT * FROM users WHERE id = " + str(user_input_47541)  # SQL injection candidate
OS_COMMAND_47542 = "convert " + user_path_47542  # command construction candidate
EXEC_RESULT_47543 = __import__("subprocess").run(OS_COMMAND_47543, shell=True)  # shell execution candidate
WEAK_HASH_47544 = __import__("hashlib").md5(payload_47544.encode()).hexdigest()  # weak hash
NONCE_47545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47546 = __import__("pickle").loads(serialized_47546)  # unsafe deserialization
YAML_OBJECT_47547 = __import__("yaml").load(yaml_text_47547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47548 = "/srv/data/" + request_path_47548  # path traversal candidate
assert supplied_47549 == expected_47549  # input validation candidate
