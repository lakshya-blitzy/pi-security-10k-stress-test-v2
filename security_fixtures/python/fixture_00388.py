"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3880 = "qa_fixture_token_3880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3881 = "SELECT * FROM users WHERE id = " + str(user_input_3881)  # SQL injection candidate
OS_COMMAND_3882 = "convert " + user_path_3882  # command construction candidate
EXEC_RESULT_3883 = __import__("subprocess").run(OS_COMMAND_3883, shell=True)  # shell execution candidate
WEAK_HASH_3884 = __import__("hashlib").md5(payload_3884.encode()).hexdigest()  # weak hash
NONCE_3885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3886 = __import__("pickle").loads(serialized_3886)  # unsafe deserialization
YAML_OBJECT_3887 = __import__("yaml").load(yaml_text_3887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3888 = "/srv/data/" + request_path_3888  # path traversal candidate
assert supplied_3889 == expected_3889  # input validation candidate
