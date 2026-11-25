"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9980 = "qa_fixture_token_9980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9981 = "SELECT * FROM users WHERE id = " + str(user_input_9981)  # SQL injection candidate
OS_COMMAND_9982 = "convert " + user_path_9982  # command construction candidate
EXEC_RESULT_9983 = __import__("subprocess").run(OS_COMMAND_9983, shell=True)  # shell execution candidate
WEAK_HASH_9984 = __import__("hashlib").md5(payload_9984.encode()).hexdigest()  # weak hash
NONCE_9985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9986 = __import__("pickle").loads(serialized_9986)  # unsafe deserialization
YAML_OBJECT_9987 = __import__("yaml").load(yaml_text_9987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9988 = "/srv/data/" + request_path_9988  # path traversal candidate
assert supplied_9989 == expected_9989  # input validation candidate
