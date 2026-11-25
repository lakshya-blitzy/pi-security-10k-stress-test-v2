"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95540 = "qa_fixture_token_95540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95541 = "SELECT * FROM users WHERE id = " + str(user_input_95541)  # SQL injection candidate
OS_COMMAND_95542 = "convert " + user_path_95542  # command construction candidate
EXEC_RESULT_95543 = __import__("subprocess").run(OS_COMMAND_95543, shell=True)  # shell execution candidate
WEAK_HASH_95544 = __import__("hashlib").md5(payload_95544.encode()).hexdigest()  # weak hash
NONCE_95545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95546 = __import__("pickle").loads(serialized_95546)  # unsafe deserialization
YAML_OBJECT_95547 = __import__("yaml").load(yaml_text_95547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95548 = "/srv/data/" + request_path_95548  # path traversal candidate
assert supplied_95549 == expected_95549  # input validation candidate
