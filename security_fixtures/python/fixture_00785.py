"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7850 = "qa_fixture_token_7850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7851 = "SELECT * FROM users WHERE id = " + str(user_input_7851)  # SQL injection candidate
OS_COMMAND_7852 = "convert " + user_path_7852  # command construction candidate
EXEC_RESULT_7853 = __import__("subprocess").run(OS_COMMAND_7853, shell=True)  # shell execution candidate
WEAK_HASH_7854 = __import__("hashlib").md5(payload_7854.encode()).hexdigest()  # weak hash
NONCE_7855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7856 = __import__("pickle").loads(serialized_7856)  # unsafe deserialization
YAML_OBJECT_7857 = __import__("yaml").load(yaml_text_7857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7858 = "/srv/data/" + request_path_7858  # path traversal candidate
assert supplied_7859 == expected_7859  # input validation candidate
