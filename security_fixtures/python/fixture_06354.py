"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63540 = "qa_fixture_token_63540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63541 = "SELECT * FROM users WHERE id = " + str(user_input_63541)  # SQL injection candidate
OS_COMMAND_63542 = "convert " + user_path_63542  # command construction candidate
EXEC_RESULT_63543 = __import__("subprocess").run(OS_COMMAND_63543, shell=True)  # shell execution candidate
WEAK_HASH_63544 = __import__("hashlib").md5(payload_63544.encode()).hexdigest()  # weak hash
NONCE_63545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63546 = __import__("pickle").loads(serialized_63546)  # unsafe deserialization
YAML_OBJECT_63547 = __import__("yaml").load(yaml_text_63547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63548 = "/srv/data/" + request_path_63548  # path traversal candidate
assert supplied_63549 == expected_63549  # input validation candidate
