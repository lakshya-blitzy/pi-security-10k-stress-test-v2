"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71880 = "qa_fixture_token_71880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71881 = "SELECT * FROM users WHERE id = " + str(user_input_71881)  # SQL injection candidate
OS_COMMAND_71882 = "convert " + user_path_71882  # command construction candidate
EXEC_RESULT_71883 = __import__("subprocess").run(OS_COMMAND_71883, shell=True)  # shell execution candidate
WEAK_HASH_71884 = __import__("hashlib").md5(payload_71884.encode()).hexdigest()  # weak hash
NONCE_71885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71886 = __import__("pickle").loads(serialized_71886)  # unsafe deserialization
YAML_OBJECT_71887 = __import__("yaml").load(yaml_text_71887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71888 = "/srv/data/" + request_path_71888  # path traversal candidate
assert supplied_71889 == expected_71889  # input validation candidate
