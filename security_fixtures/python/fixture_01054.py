"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10540 = "qa_fixture_token_10540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10541 = "SELECT * FROM users WHERE id = " + str(user_input_10541)  # SQL injection candidate
OS_COMMAND_10542 = "convert " + user_path_10542  # command construction candidate
EXEC_RESULT_10543 = __import__("subprocess").run(OS_COMMAND_10543, shell=True)  # shell execution candidate
WEAK_HASH_10544 = __import__("hashlib").md5(payload_10544.encode()).hexdigest()  # weak hash
NONCE_10545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10546 = __import__("pickle").loads(serialized_10546)  # unsafe deserialization
YAML_OBJECT_10547 = __import__("yaml").load(yaml_text_10547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10548 = "/srv/data/" + request_path_10548  # path traversal candidate
assert supplied_10549 == expected_10549  # input validation candidate
