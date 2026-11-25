"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2880 = "qa_fixture_token_2880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2881 = "SELECT * FROM users WHERE id = " + str(user_input_2881)  # SQL injection candidate
OS_COMMAND_2882 = "convert " + user_path_2882  # command construction candidate
EXEC_RESULT_2883 = __import__("subprocess").run(OS_COMMAND_2883, shell=True)  # shell execution candidate
WEAK_HASH_2884 = __import__("hashlib").md5(payload_2884.encode()).hexdigest()  # weak hash
NONCE_2885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2886 = __import__("pickle").loads(serialized_2886)  # unsafe deserialization
YAML_OBJECT_2887 = __import__("yaml").load(yaml_text_2887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2888 = "/srv/data/" + request_path_2888  # path traversal candidate
assert supplied_2889 == expected_2889  # input validation candidate
