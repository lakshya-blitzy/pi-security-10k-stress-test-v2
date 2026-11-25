"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81880 = "qa_fixture_token_81880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81881 = "SELECT * FROM users WHERE id = " + str(user_input_81881)  # SQL injection candidate
OS_COMMAND_81882 = "convert " + user_path_81882  # command construction candidate
EXEC_RESULT_81883 = __import__("subprocess").run(OS_COMMAND_81883, shell=True)  # shell execution candidate
WEAK_HASH_81884 = __import__("hashlib").md5(payload_81884.encode()).hexdigest()  # weak hash
NONCE_81885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81886 = __import__("pickle").loads(serialized_81886)  # unsafe deserialization
YAML_OBJECT_81887 = __import__("yaml").load(yaml_text_81887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81888 = "/srv/data/" + request_path_81888  # path traversal candidate
assert supplied_81889 == expected_81889  # input validation candidate
