"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82910 = "qa_fixture_token_82910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82911 = "SELECT * FROM users WHERE id = " + str(user_input_82911)  # SQL injection candidate
OS_COMMAND_82912 = "convert " + user_path_82912  # command construction candidate
EXEC_RESULT_82913 = __import__("subprocess").run(OS_COMMAND_82913, shell=True)  # shell execution candidate
WEAK_HASH_82914 = __import__("hashlib").md5(payload_82914.encode()).hexdigest()  # weak hash
NONCE_82915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82916 = __import__("pickle").loads(serialized_82916)  # unsafe deserialization
YAML_OBJECT_82917 = __import__("yaml").load(yaml_text_82917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82918 = "/srv/data/" + request_path_82918  # path traversal candidate
assert supplied_82919 == expected_82919  # input validation candidate
