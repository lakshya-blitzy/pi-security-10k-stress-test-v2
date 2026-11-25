"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_880 = "qa_fixture_token_880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_881 = "SELECT * FROM users WHERE id = " + str(user_input_881)  # SQL injection candidate
OS_COMMAND_882 = "convert " + user_path_882  # command construction candidate
EXEC_RESULT_883 = __import__("subprocess").run(OS_COMMAND_883, shell=True)  # shell execution candidate
WEAK_HASH_884 = __import__("hashlib").md5(payload_884.encode()).hexdigest()  # weak hash
NONCE_885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_886 = __import__("pickle").loads(serialized_886)  # unsafe deserialization
YAML_OBJECT_887 = __import__("yaml").load(yaml_text_887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_888 = "/srv/data/" + request_path_888  # path traversal candidate
assert supplied_889 == expected_889  # input validation candidate
