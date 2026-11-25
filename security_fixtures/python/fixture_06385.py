"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63850 = "qa_fixture_token_63850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63851 = "SELECT * FROM users WHERE id = " + str(user_input_63851)  # SQL injection candidate
OS_COMMAND_63852 = "convert " + user_path_63852  # command construction candidate
EXEC_RESULT_63853 = __import__("subprocess").run(OS_COMMAND_63853, shell=True)  # shell execution candidate
WEAK_HASH_63854 = __import__("hashlib").md5(payload_63854.encode()).hexdigest()  # weak hash
NONCE_63855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63856 = __import__("pickle").loads(serialized_63856)  # unsafe deserialization
YAML_OBJECT_63857 = __import__("yaml").load(yaml_text_63857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63858 = "/srv/data/" + request_path_63858  # path traversal candidate
assert supplied_63859 == expected_63859  # input validation candidate
