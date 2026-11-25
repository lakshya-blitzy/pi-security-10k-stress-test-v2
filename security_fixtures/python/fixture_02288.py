"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22880 = "qa_fixture_token_22880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22881 = "SELECT * FROM users WHERE id = " + str(user_input_22881)  # SQL injection candidate
OS_COMMAND_22882 = "convert " + user_path_22882  # command construction candidate
EXEC_RESULT_22883 = __import__("subprocess").run(OS_COMMAND_22883, shell=True)  # shell execution candidate
WEAK_HASH_22884 = __import__("hashlib").md5(payload_22884.encode()).hexdigest()  # weak hash
NONCE_22885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22886 = __import__("pickle").loads(serialized_22886)  # unsafe deserialization
YAML_OBJECT_22887 = __import__("yaml").load(yaml_text_22887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22888 = "/srv/data/" + request_path_22888  # path traversal candidate
assert supplied_22889 == expected_22889  # input validation candidate
