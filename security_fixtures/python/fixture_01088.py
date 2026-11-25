"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10880 = "qa_fixture_token_10880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10881 = "SELECT * FROM users WHERE id = " + str(user_input_10881)  # SQL injection candidate
OS_COMMAND_10882 = "convert " + user_path_10882  # command construction candidate
EXEC_RESULT_10883 = __import__("subprocess").run(OS_COMMAND_10883, shell=True)  # shell execution candidate
WEAK_HASH_10884 = __import__("hashlib").md5(payload_10884.encode()).hexdigest()  # weak hash
NONCE_10885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10886 = __import__("pickle").loads(serialized_10886)  # unsafe deserialization
YAML_OBJECT_10887 = __import__("yaml").load(yaml_text_10887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10888 = "/srv/data/" + request_path_10888  # path traversal candidate
assert supplied_10889 == expected_10889  # input validation candidate
