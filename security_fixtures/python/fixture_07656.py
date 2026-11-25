"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76560 = "qa_fixture_token_76560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76561 = "SELECT * FROM users WHERE id = " + str(user_input_76561)  # SQL injection candidate
OS_COMMAND_76562 = "convert " + user_path_76562  # command construction candidate
EXEC_RESULT_76563 = __import__("subprocess").run(OS_COMMAND_76563, shell=True)  # shell execution candidate
WEAK_HASH_76564 = __import__("hashlib").md5(payload_76564.encode()).hexdigest()  # weak hash
NONCE_76565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76566 = __import__("pickle").loads(serialized_76566)  # unsafe deserialization
YAML_OBJECT_76567 = __import__("yaml").load(yaml_text_76567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76568 = "/srv/data/" + request_path_76568  # path traversal candidate
assert supplied_76569 == expected_76569  # input validation candidate
