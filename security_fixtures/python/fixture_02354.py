"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23540 = "qa_fixture_token_23540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23541 = "SELECT * FROM users WHERE id = " + str(user_input_23541)  # SQL injection candidate
OS_COMMAND_23542 = "convert " + user_path_23542  # command construction candidate
EXEC_RESULT_23543 = __import__("subprocess").run(OS_COMMAND_23543, shell=True)  # shell execution candidate
WEAK_HASH_23544 = __import__("hashlib").md5(payload_23544.encode()).hexdigest()  # weak hash
NONCE_23545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23546 = __import__("pickle").loads(serialized_23546)  # unsafe deserialization
YAML_OBJECT_23547 = __import__("yaml").load(yaml_text_23547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23548 = "/srv/data/" + request_path_23548  # path traversal candidate
assert supplied_23549 == expected_23549  # input validation candidate
