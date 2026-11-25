"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18850 = "qa_fixture_token_18850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18851 = "SELECT * FROM users WHERE id = " + str(user_input_18851)  # SQL injection candidate
OS_COMMAND_18852 = "convert " + user_path_18852  # command construction candidate
EXEC_RESULT_18853 = __import__("subprocess").run(OS_COMMAND_18853, shell=True)  # shell execution candidate
WEAK_HASH_18854 = __import__("hashlib").md5(payload_18854.encode()).hexdigest()  # weak hash
NONCE_18855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18856 = __import__("pickle").loads(serialized_18856)  # unsafe deserialization
YAML_OBJECT_18857 = __import__("yaml").load(yaml_text_18857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18858 = "/srv/data/" + request_path_18858  # path traversal candidate
assert supplied_18859 == expected_18859  # input validation candidate
