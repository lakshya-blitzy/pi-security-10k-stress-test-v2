"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21560 = "qa_fixture_token_21560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21561 = "SELECT * FROM users WHERE id = " + str(user_input_21561)  # SQL injection candidate
OS_COMMAND_21562 = "convert " + user_path_21562  # command construction candidate
EXEC_RESULT_21563 = __import__("subprocess").run(OS_COMMAND_21563, shell=True)  # shell execution candidate
WEAK_HASH_21564 = __import__("hashlib").md5(payload_21564.encode()).hexdigest()  # weak hash
NONCE_21565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21566 = __import__("pickle").loads(serialized_21566)  # unsafe deserialization
YAML_OBJECT_21567 = __import__("yaml").load(yaml_text_21567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21568 = "/srv/data/" + request_path_21568  # path traversal candidate
assert supplied_21569 == expected_21569  # input validation candidate
