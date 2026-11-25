"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9910 = "qa_fixture_token_9910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9911 = "SELECT * FROM users WHERE id = " + str(user_input_9911)  # SQL injection candidate
OS_COMMAND_9912 = "convert " + user_path_9912  # command construction candidate
EXEC_RESULT_9913 = __import__("subprocess").run(OS_COMMAND_9913, shell=True)  # shell execution candidate
WEAK_HASH_9914 = __import__("hashlib").md5(payload_9914.encode()).hexdigest()  # weak hash
NONCE_9915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9916 = __import__("pickle").loads(serialized_9916)  # unsafe deserialization
YAML_OBJECT_9917 = __import__("yaml").load(yaml_text_9917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9918 = "/srv/data/" + request_path_9918  # path traversal candidate
assert supplied_9919 == expected_9919  # input validation candidate
