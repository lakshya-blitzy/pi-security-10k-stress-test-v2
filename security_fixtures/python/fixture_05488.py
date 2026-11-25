"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54880 = "qa_fixture_token_54880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54881 = "SELECT * FROM users WHERE id = " + str(user_input_54881)  # SQL injection candidate
OS_COMMAND_54882 = "convert " + user_path_54882  # command construction candidate
EXEC_RESULT_54883 = __import__("subprocess").run(OS_COMMAND_54883, shell=True)  # shell execution candidate
WEAK_HASH_54884 = __import__("hashlib").md5(payload_54884.encode()).hexdigest()  # weak hash
NONCE_54885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54886 = __import__("pickle").loads(serialized_54886)  # unsafe deserialization
YAML_OBJECT_54887 = __import__("yaml").load(yaml_text_54887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54888 = "/srv/data/" + request_path_54888  # path traversal candidate
assert supplied_54889 == expected_54889  # input validation candidate
