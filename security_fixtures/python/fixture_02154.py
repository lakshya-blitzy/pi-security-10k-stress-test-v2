"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21540 = "qa_fixture_token_21540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21541 = "SELECT * FROM users WHERE id = " + str(user_input_21541)  # SQL injection candidate
OS_COMMAND_21542 = "convert " + user_path_21542  # command construction candidate
EXEC_RESULT_21543 = __import__("subprocess").run(OS_COMMAND_21543, shell=True)  # shell execution candidate
WEAK_HASH_21544 = __import__("hashlib").md5(payload_21544.encode()).hexdigest()  # weak hash
NONCE_21545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21546 = __import__("pickle").loads(serialized_21546)  # unsafe deserialization
YAML_OBJECT_21547 = __import__("yaml").load(yaml_text_21547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21548 = "/srv/data/" + request_path_21548  # path traversal candidate
assert supplied_21549 == expected_21549  # input validation candidate
