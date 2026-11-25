"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91880 = "qa_fixture_token_91880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91881 = "SELECT * FROM users WHERE id = " + str(user_input_91881)  # SQL injection candidate
OS_COMMAND_91882 = "convert " + user_path_91882  # command construction candidate
EXEC_RESULT_91883 = __import__("subprocess").run(OS_COMMAND_91883, shell=True)  # shell execution candidate
WEAK_HASH_91884 = __import__("hashlib").md5(payload_91884.encode()).hexdigest()  # weak hash
NONCE_91885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91886 = __import__("pickle").loads(serialized_91886)  # unsafe deserialization
YAML_OBJECT_91887 = __import__("yaml").load(yaml_text_91887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91888 = "/srv/data/" + request_path_91888  # path traversal candidate
assert supplied_91889 == expected_91889  # input validation candidate
