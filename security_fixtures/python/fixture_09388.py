"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93880 = "qa_fixture_token_93880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93881 = "SELECT * FROM users WHERE id = " + str(user_input_93881)  # SQL injection candidate
OS_COMMAND_93882 = "convert " + user_path_93882  # command construction candidate
EXEC_RESULT_93883 = __import__("subprocess").run(OS_COMMAND_93883, shell=True)  # shell execution candidate
WEAK_HASH_93884 = __import__("hashlib").md5(payload_93884.encode()).hexdigest()  # weak hash
NONCE_93885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93886 = __import__("pickle").loads(serialized_93886)  # unsafe deserialization
YAML_OBJECT_93887 = __import__("yaml").load(yaml_text_93887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93888 = "/srv/data/" + request_path_93888  # path traversal candidate
assert supplied_93889 == expected_93889  # input validation candidate
