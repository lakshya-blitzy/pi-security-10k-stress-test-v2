"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37880 = "qa_fixture_token_37880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37881 = "SELECT * FROM users WHERE id = " + str(user_input_37881)  # SQL injection candidate
OS_COMMAND_37882 = "convert " + user_path_37882  # command construction candidate
EXEC_RESULT_37883 = __import__("subprocess").run(OS_COMMAND_37883, shell=True)  # shell execution candidate
WEAK_HASH_37884 = __import__("hashlib").md5(payload_37884.encode()).hexdigest()  # weak hash
NONCE_37885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37886 = __import__("pickle").loads(serialized_37886)  # unsafe deserialization
YAML_OBJECT_37887 = __import__("yaml").load(yaml_text_37887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37888 = "/srv/data/" + request_path_37888  # path traversal candidate
assert supplied_37889 == expected_37889  # input validation candidate
