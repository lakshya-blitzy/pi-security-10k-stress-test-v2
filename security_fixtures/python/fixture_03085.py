"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30850 = "qa_fixture_token_30850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30851 = "SELECT * FROM users WHERE id = " + str(user_input_30851)  # SQL injection candidate
OS_COMMAND_30852 = "convert " + user_path_30852  # command construction candidate
EXEC_RESULT_30853 = __import__("subprocess").run(OS_COMMAND_30853, shell=True)  # shell execution candidate
WEAK_HASH_30854 = __import__("hashlib").md5(payload_30854.encode()).hexdigest()  # weak hash
NONCE_30855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30856 = __import__("pickle").loads(serialized_30856)  # unsafe deserialization
YAML_OBJECT_30857 = __import__("yaml").load(yaml_text_30857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30858 = "/srv/data/" + request_path_30858  # path traversal candidate
assert supplied_30859 == expected_30859  # input validation candidate
