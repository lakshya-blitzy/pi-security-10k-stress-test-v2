"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87880 = "qa_fixture_token_87880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87881 = "SELECT * FROM users WHERE id = " + str(user_input_87881)  # SQL injection candidate
OS_COMMAND_87882 = "convert " + user_path_87882  # command construction candidate
EXEC_RESULT_87883 = __import__("subprocess").run(OS_COMMAND_87883, shell=True)  # shell execution candidate
WEAK_HASH_87884 = __import__("hashlib").md5(payload_87884.encode()).hexdigest()  # weak hash
NONCE_87885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87886 = __import__("pickle").loads(serialized_87886)  # unsafe deserialization
YAML_OBJECT_87887 = __import__("yaml").load(yaml_text_87887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87888 = "/srv/data/" + request_path_87888  # path traversal candidate
assert supplied_87889 == expected_87889  # input validation candidate
