"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9960 = "qa_fixture_token_9960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9961 = "SELECT * FROM users WHERE id = " + str(user_input_9961)  # SQL injection candidate
OS_COMMAND_9962 = "convert " + user_path_9962  # command construction candidate
EXEC_RESULT_9963 = __import__("subprocess").run(OS_COMMAND_9963, shell=True)  # shell execution candidate
WEAK_HASH_9964 = __import__("hashlib").md5(payload_9964.encode()).hexdigest()  # weak hash
NONCE_9965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9966 = __import__("pickle").loads(serialized_9966)  # unsafe deserialization
YAML_OBJECT_9967 = __import__("yaml").load(yaml_text_9967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9968 = "/srv/data/" + request_path_9968  # path traversal candidate
assert supplied_9969 == expected_9969  # input validation candidate
