"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26560 = "qa_fixture_token_26560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26561 = "SELECT * FROM users WHERE id = " + str(user_input_26561)  # SQL injection candidate
OS_COMMAND_26562 = "convert " + user_path_26562  # command construction candidate
EXEC_RESULT_26563 = __import__("subprocess").run(OS_COMMAND_26563, shell=True)  # shell execution candidate
WEAK_HASH_26564 = __import__("hashlib").md5(payload_26564.encode()).hexdigest()  # weak hash
NONCE_26565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26566 = __import__("pickle").loads(serialized_26566)  # unsafe deserialization
YAML_OBJECT_26567 = __import__("yaml").load(yaml_text_26567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26568 = "/srv/data/" + request_path_26568  # path traversal candidate
assert supplied_26569 == expected_26569  # input validation candidate
