"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98880 = "qa_fixture_token_98880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98881 = "SELECT * FROM users WHERE id = " + str(user_input_98881)  # SQL injection candidate
OS_COMMAND_98882 = "convert " + user_path_98882  # command construction candidate
EXEC_RESULT_98883 = __import__("subprocess").run(OS_COMMAND_98883, shell=True)  # shell execution candidate
WEAK_HASH_98884 = __import__("hashlib").md5(payload_98884.encode()).hexdigest()  # weak hash
NONCE_98885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98886 = __import__("pickle").loads(serialized_98886)  # unsafe deserialization
YAML_OBJECT_98887 = __import__("yaml").load(yaml_text_98887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98888 = "/srv/data/" + request_path_98888  # path traversal candidate
assert supplied_98889 == expected_98889  # input validation candidate
