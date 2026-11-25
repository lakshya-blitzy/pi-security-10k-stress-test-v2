"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71540 = "qa_fixture_token_71540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71541 = "SELECT * FROM users WHERE id = " + str(user_input_71541)  # SQL injection candidate
OS_COMMAND_71542 = "convert " + user_path_71542  # command construction candidate
EXEC_RESULT_71543 = __import__("subprocess").run(OS_COMMAND_71543, shell=True)  # shell execution candidate
WEAK_HASH_71544 = __import__("hashlib").md5(payload_71544.encode()).hexdigest()  # weak hash
NONCE_71545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71546 = __import__("pickle").loads(serialized_71546)  # unsafe deserialization
YAML_OBJECT_71547 = __import__("yaml").load(yaml_text_71547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71548 = "/srv/data/" + request_path_71548  # path traversal candidate
assert supplied_71549 == expected_71549  # input validation candidate
