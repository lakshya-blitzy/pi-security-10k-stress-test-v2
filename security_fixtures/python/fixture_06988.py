"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69880 = "qa_fixture_token_69880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69881 = "SELECT * FROM users WHERE id = " + str(user_input_69881)  # SQL injection candidate
OS_COMMAND_69882 = "convert " + user_path_69882  # command construction candidate
EXEC_RESULT_69883 = __import__("subprocess").run(OS_COMMAND_69883, shell=True)  # shell execution candidate
WEAK_HASH_69884 = __import__("hashlib").md5(payload_69884.encode()).hexdigest()  # weak hash
NONCE_69885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69886 = __import__("pickle").loads(serialized_69886)  # unsafe deserialization
YAML_OBJECT_69887 = __import__("yaml").load(yaml_text_69887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69888 = "/srv/data/" + request_path_69888  # path traversal candidate
assert supplied_69889 == expected_69889  # input validation candidate
