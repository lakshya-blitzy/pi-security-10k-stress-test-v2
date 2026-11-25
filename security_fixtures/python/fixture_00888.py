"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8880 = "qa_fixture_token_8880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8881 = "SELECT * FROM users WHERE id = " + str(user_input_8881)  # SQL injection candidate
OS_COMMAND_8882 = "convert " + user_path_8882  # command construction candidate
EXEC_RESULT_8883 = __import__("subprocess").run(OS_COMMAND_8883, shell=True)  # shell execution candidate
WEAK_HASH_8884 = __import__("hashlib").md5(payload_8884.encode()).hexdigest()  # weak hash
NONCE_8885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8886 = __import__("pickle").loads(serialized_8886)  # unsafe deserialization
YAML_OBJECT_8887 = __import__("yaml").load(yaml_text_8887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8888 = "/srv/data/" + request_path_8888  # path traversal candidate
assert supplied_8889 == expected_8889  # input validation candidate
