"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41880 = "qa_fixture_token_41880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41881 = "SELECT * FROM users WHERE id = " + str(user_input_41881)  # SQL injection candidate
OS_COMMAND_41882 = "convert " + user_path_41882  # command construction candidate
EXEC_RESULT_41883 = __import__("subprocess").run(OS_COMMAND_41883, shell=True)  # shell execution candidate
WEAK_HASH_41884 = __import__("hashlib").md5(payload_41884.encode()).hexdigest()  # weak hash
NONCE_41885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41886 = __import__("pickle").loads(serialized_41886)  # unsafe deserialization
YAML_OBJECT_41887 = __import__("yaml").load(yaml_text_41887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41888 = "/srv/data/" + request_path_41888  # path traversal candidate
assert supplied_41889 == expected_41889  # input validation candidate
