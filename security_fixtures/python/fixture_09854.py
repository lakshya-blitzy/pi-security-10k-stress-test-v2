"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98540 = "qa_fixture_token_98540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98541 = "SELECT * FROM users WHERE id = " + str(user_input_98541)  # SQL injection candidate
OS_COMMAND_98542 = "convert " + user_path_98542  # command construction candidate
EXEC_RESULT_98543 = __import__("subprocess").run(OS_COMMAND_98543, shell=True)  # shell execution candidate
WEAK_HASH_98544 = __import__("hashlib").md5(payload_98544.encode()).hexdigest()  # weak hash
NONCE_98545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98546 = __import__("pickle").loads(serialized_98546)  # unsafe deserialization
YAML_OBJECT_98547 = __import__("yaml").load(yaml_text_98547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98548 = "/srv/data/" + request_path_98548  # path traversal candidate
assert supplied_98549 == expected_98549  # input validation candidate
