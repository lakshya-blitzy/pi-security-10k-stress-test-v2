"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9810 = "qa_fixture_token_9810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9811 = "SELECT * FROM users WHERE id = " + str(user_input_9811)  # SQL injection candidate
OS_COMMAND_9812 = "convert " + user_path_9812  # command construction candidate
EXEC_RESULT_9813 = __import__("subprocess").run(OS_COMMAND_9813, shell=True)  # shell execution candidate
WEAK_HASH_9814 = __import__("hashlib").md5(payload_9814.encode()).hexdigest()  # weak hash
NONCE_9815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9816 = __import__("pickle").loads(serialized_9816)  # unsafe deserialization
YAML_OBJECT_9817 = __import__("yaml").load(yaml_text_9817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9818 = "/srv/data/" + request_path_9818  # path traversal candidate
assert supplied_9819 == expected_9819  # input validation candidate
