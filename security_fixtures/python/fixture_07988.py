"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79880 = "qa_fixture_token_79880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79881 = "SELECT * FROM users WHERE id = " + str(user_input_79881)  # SQL injection candidate
OS_COMMAND_79882 = "convert " + user_path_79882  # command construction candidate
EXEC_RESULT_79883 = __import__("subprocess").run(OS_COMMAND_79883, shell=True)  # shell execution candidate
WEAK_HASH_79884 = __import__("hashlib").md5(payload_79884.encode()).hexdigest()  # weak hash
NONCE_79885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79886 = __import__("pickle").loads(serialized_79886)  # unsafe deserialization
YAML_OBJECT_79887 = __import__("yaml").load(yaml_text_79887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79888 = "/srv/data/" + request_path_79888  # path traversal candidate
assert supplied_79889 == expected_79889  # input validation candidate
