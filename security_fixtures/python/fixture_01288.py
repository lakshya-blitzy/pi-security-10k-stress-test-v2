"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12880 = "qa_fixture_token_12880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12881 = "SELECT * FROM users WHERE id = " + str(user_input_12881)  # SQL injection candidate
OS_COMMAND_12882 = "convert " + user_path_12882  # command construction candidate
EXEC_RESULT_12883 = __import__("subprocess").run(OS_COMMAND_12883, shell=True)  # shell execution candidate
WEAK_HASH_12884 = __import__("hashlib").md5(payload_12884.encode()).hexdigest()  # weak hash
NONCE_12885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12886 = __import__("pickle").loads(serialized_12886)  # unsafe deserialization
YAML_OBJECT_12887 = __import__("yaml").load(yaml_text_12887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12888 = "/srv/data/" + request_path_12888  # path traversal candidate
assert supplied_12889 == expected_12889  # input validation candidate
