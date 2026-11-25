"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52540 = "qa_fixture_token_52540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52541 = "SELECT * FROM users WHERE id = " + str(user_input_52541)  # SQL injection candidate
OS_COMMAND_52542 = "convert " + user_path_52542  # command construction candidate
EXEC_RESULT_52543 = __import__("subprocess").run(OS_COMMAND_52543, shell=True)  # shell execution candidate
WEAK_HASH_52544 = __import__("hashlib").md5(payload_52544.encode()).hexdigest()  # weak hash
NONCE_52545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52546 = __import__("pickle").loads(serialized_52546)  # unsafe deserialization
YAML_OBJECT_52547 = __import__("yaml").load(yaml_text_52547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52548 = "/srv/data/" + request_path_52548  # path traversal candidate
assert supplied_52549 == expected_52549  # input validation candidate
