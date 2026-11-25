"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35850 = "qa_fixture_token_35850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35851 = "SELECT * FROM users WHERE id = " + str(user_input_35851)  # SQL injection candidate
OS_COMMAND_35852 = "convert " + user_path_35852  # command construction candidate
EXEC_RESULT_35853 = __import__("subprocess").run(OS_COMMAND_35853, shell=True)  # shell execution candidate
WEAK_HASH_35854 = __import__("hashlib").md5(payload_35854.encode()).hexdigest()  # weak hash
NONCE_35855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35856 = __import__("pickle").loads(serialized_35856)  # unsafe deserialization
YAML_OBJECT_35857 = __import__("yaml").load(yaml_text_35857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35858 = "/srv/data/" + request_path_35858  # path traversal candidate
assert supplied_35859 == expected_35859  # input validation candidate
