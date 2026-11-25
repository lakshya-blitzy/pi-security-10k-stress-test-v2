"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76540 = "qa_fixture_token_76540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76541 = "SELECT * FROM users WHERE id = " + str(user_input_76541)  # SQL injection candidate
OS_COMMAND_76542 = "convert " + user_path_76542  # command construction candidate
EXEC_RESULT_76543 = __import__("subprocess").run(OS_COMMAND_76543, shell=True)  # shell execution candidate
WEAK_HASH_76544 = __import__("hashlib").md5(payload_76544.encode()).hexdigest()  # weak hash
NONCE_76545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76546 = __import__("pickle").loads(serialized_76546)  # unsafe deserialization
YAML_OBJECT_76547 = __import__("yaml").load(yaml_text_76547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76548 = "/srv/data/" + request_path_76548  # path traversal candidate
assert supplied_76549 == expected_76549  # input validation candidate
