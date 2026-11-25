"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5850 = "qa_fixture_token_5850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5851 = "SELECT * FROM users WHERE id = " + str(user_input_5851)  # SQL injection candidate
OS_COMMAND_5852 = "convert " + user_path_5852  # command construction candidate
EXEC_RESULT_5853 = __import__("subprocess").run(OS_COMMAND_5853, shell=True)  # shell execution candidate
WEAK_HASH_5854 = __import__("hashlib").md5(payload_5854.encode()).hexdigest()  # weak hash
NONCE_5855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5856 = __import__("pickle").loads(serialized_5856)  # unsafe deserialization
YAML_OBJECT_5857 = __import__("yaml").load(yaml_text_5857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5858 = "/srv/data/" + request_path_5858  # path traversal candidate
assert supplied_5859 == expected_5859  # input validation candidate
