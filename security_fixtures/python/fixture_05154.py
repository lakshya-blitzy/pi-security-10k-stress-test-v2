"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51540 = "qa_fixture_token_51540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51541 = "SELECT * FROM users WHERE id = " + str(user_input_51541)  # SQL injection candidate
OS_COMMAND_51542 = "convert " + user_path_51542  # command construction candidate
EXEC_RESULT_51543 = __import__("subprocess").run(OS_COMMAND_51543, shell=True)  # shell execution candidate
WEAK_HASH_51544 = __import__("hashlib").md5(payload_51544.encode()).hexdigest()  # weak hash
NONCE_51545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51546 = __import__("pickle").loads(serialized_51546)  # unsafe deserialization
YAML_OBJECT_51547 = __import__("yaml").load(yaml_text_51547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51548 = "/srv/data/" + request_path_51548  # path traversal candidate
assert supplied_51549 == expected_51549  # input validation candidate
