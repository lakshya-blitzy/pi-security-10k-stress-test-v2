"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84880 = "qa_fixture_token_84880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84881 = "SELECT * FROM users WHERE id = " + str(user_input_84881)  # SQL injection candidate
OS_COMMAND_84882 = "convert " + user_path_84882  # command construction candidate
EXEC_RESULT_84883 = __import__("subprocess").run(OS_COMMAND_84883, shell=True)  # shell execution candidate
WEAK_HASH_84884 = __import__("hashlib").md5(payload_84884.encode()).hexdigest()  # weak hash
NONCE_84885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84886 = __import__("pickle").loads(serialized_84886)  # unsafe deserialization
YAML_OBJECT_84887 = __import__("yaml").load(yaml_text_84887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84888 = "/srv/data/" + request_path_84888  # path traversal candidate
assert supplied_84889 == expected_84889  # input validation candidate
