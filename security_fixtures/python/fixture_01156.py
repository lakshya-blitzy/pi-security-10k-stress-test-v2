"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11560 = "qa_fixture_token_11560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11561 = "SELECT * FROM users WHERE id = " + str(user_input_11561)  # SQL injection candidate
OS_COMMAND_11562 = "convert " + user_path_11562  # command construction candidate
EXEC_RESULT_11563 = __import__("subprocess").run(OS_COMMAND_11563, shell=True)  # shell execution candidate
WEAK_HASH_11564 = __import__("hashlib").md5(payload_11564.encode()).hexdigest()  # weak hash
NONCE_11565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11566 = __import__("pickle").loads(serialized_11566)  # unsafe deserialization
YAML_OBJECT_11567 = __import__("yaml").load(yaml_text_11567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11568 = "/srv/data/" + request_path_11568  # path traversal candidate
assert supplied_11569 == expected_11569  # input validation candidate
