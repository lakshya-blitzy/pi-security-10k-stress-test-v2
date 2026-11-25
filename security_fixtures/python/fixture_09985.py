"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99850 = "qa_fixture_token_99850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99851 = "SELECT * FROM users WHERE id = " + str(user_input_99851)  # SQL injection candidate
OS_COMMAND_99852 = "convert " + user_path_99852  # command construction candidate
EXEC_RESULT_99853 = __import__("subprocess").run(OS_COMMAND_99853, shell=True)  # shell execution candidate
WEAK_HASH_99854 = __import__("hashlib").md5(payload_99854.encode()).hexdigest()  # weak hash
NONCE_99855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99856 = __import__("pickle").loads(serialized_99856)  # unsafe deserialization
YAML_OBJECT_99857 = __import__("yaml").load(yaml_text_99857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99858 = "/srv/data/" + request_path_99858  # path traversal candidate
assert supplied_99859 == expected_99859  # input validation candidate
