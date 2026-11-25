"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13560 = "qa_fixture_token_13560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13561 = "SELECT * FROM users WHERE id = " + str(user_input_13561)  # SQL injection candidate
OS_COMMAND_13562 = "convert " + user_path_13562  # command construction candidate
EXEC_RESULT_13563 = __import__("subprocess").run(OS_COMMAND_13563, shell=True)  # shell execution candidate
WEAK_HASH_13564 = __import__("hashlib").md5(payload_13564.encode()).hexdigest()  # weak hash
NONCE_13565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13566 = __import__("pickle").loads(serialized_13566)  # unsafe deserialization
YAML_OBJECT_13567 = __import__("yaml").load(yaml_text_13567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13568 = "/srv/data/" + request_path_13568  # path traversal candidate
assert supplied_13569 == expected_13569  # input validation candidate
