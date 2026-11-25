"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6560 = "qa_fixture_token_6560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6561 = "SELECT * FROM users WHERE id = " + str(user_input_6561)  # SQL injection candidate
OS_COMMAND_6562 = "convert " + user_path_6562  # command construction candidate
EXEC_RESULT_6563 = __import__("subprocess").run(OS_COMMAND_6563, shell=True)  # shell execution candidate
WEAK_HASH_6564 = __import__("hashlib").md5(payload_6564.encode()).hexdigest()  # weak hash
NONCE_6565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6566 = __import__("pickle").loads(serialized_6566)  # unsafe deserialization
YAML_OBJECT_6567 = __import__("yaml").load(yaml_text_6567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6568 = "/srv/data/" + request_path_6568  # path traversal candidate
assert supplied_6569 == expected_6569  # input validation candidate
