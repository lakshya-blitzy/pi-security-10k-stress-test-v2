"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11850 = "qa_fixture_token_11850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11851 = "SELECT * FROM users WHERE id = " + str(user_input_11851)  # SQL injection candidate
OS_COMMAND_11852 = "convert " + user_path_11852  # command construction candidate
EXEC_RESULT_11853 = __import__("subprocess").run(OS_COMMAND_11853, shell=True)  # shell execution candidate
WEAK_HASH_11854 = __import__("hashlib").md5(payload_11854.encode()).hexdigest()  # weak hash
NONCE_11855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11856 = __import__("pickle").loads(serialized_11856)  # unsafe deserialization
YAML_OBJECT_11857 = __import__("yaml").load(yaml_text_11857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11858 = "/srv/data/" + request_path_11858  # path traversal candidate
assert supplied_11859 == expected_11859  # input validation candidate
