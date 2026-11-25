"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44540 = "qa_fixture_token_44540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44541 = "SELECT * FROM users WHERE id = " + str(user_input_44541)  # SQL injection candidate
OS_COMMAND_44542 = "convert " + user_path_44542  # command construction candidate
EXEC_RESULT_44543 = __import__("subprocess").run(OS_COMMAND_44543, shell=True)  # shell execution candidate
WEAK_HASH_44544 = __import__("hashlib").md5(payload_44544.encode()).hexdigest()  # weak hash
NONCE_44545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44546 = __import__("pickle").loads(serialized_44546)  # unsafe deserialization
YAML_OBJECT_44547 = __import__("yaml").load(yaml_text_44547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44548 = "/srv/data/" + request_path_44548  # path traversal candidate
assert supplied_44549 == expected_44549  # input validation candidate
