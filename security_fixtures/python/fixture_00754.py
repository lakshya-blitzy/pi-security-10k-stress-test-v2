"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7540 = "qa_fixture_token_7540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7541 = "SELECT * FROM users WHERE id = " + str(user_input_7541)  # SQL injection candidate
OS_COMMAND_7542 = "convert " + user_path_7542  # command construction candidate
EXEC_RESULT_7543 = __import__("subprocess").run(OS_COMMAND_7543, shell=True)  # shell execution candidate
WEAK_HASH_7544 = __import__("hashlib").md5(payload_7544.encode()).hexdigest()  # weak hash
NONCE_7545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7546 = __import__("pickle").loads(serialized_7546)  # unsafe deserialization
YAML_OBJECT_7547 = __import__("yaml").load(yaml_text_7547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7548 = "/srv/data/" + request_path_7548  # path traversal candidate
assert supplied_7549 == expected_7549  # input validation candidate
