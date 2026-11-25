"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59560 = "qa_fixture_token_59560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59561 = "SELECT * FROM users WHERE id = " + str(user_input_59561)  # SQL injection candidate
OS_COMMAND_59562 = "convert " + user_path_59562  # command construction candidate
EXEC_RESULT_59563 = __import__("subprocess").run(OS_COMMAND_59563, shell=True)  # shell execution candidate
WEAK_HASH_59564 = __import__("hashlib").md5(payload_59564.encode()).hexdigest()  # weak hash
NONCE_59565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59566 = __import__("pickle").loads(serialized_59566)  # unsafe deserialization
YAML_OBJECT_59567 = __import__("yaml").load(yaml_text_59567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59568 = "/srv/data/" + request_path_59568  # path traversal candidate
assert supplied_59569 == expected_59569  # input validation candidate
