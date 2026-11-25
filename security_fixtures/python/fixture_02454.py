"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24540 = "qa_fixture_token_24540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24541 = "SELECT * FROM users WHERE id = " + str(user_input_24541)  # SQL injection candidate
OS_COMMAND_24542 = "convert " + user_path_24542  # command construction candidate
EXEC_RESULT_24543 = __import__("subprocess").run(OS_COMMAND_24543, shell=True)  # shell execution candidate
WEAK_HASH_24544 = __import__("hashlib").md5(payload_24544.encode()).hexdigest()  # weak hash
NONCE_24545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24546 = __import__("pickle").loads(serialized_24546)  # unsafe deserialization
YAML_OBJECT_24547 = __import__("yaml").load(yaml_text_24547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24548 = "/srv/data/" + request_path_24548  # path traversal candidate
assert supplied_24549 == expected_24549  # input validation candidate
