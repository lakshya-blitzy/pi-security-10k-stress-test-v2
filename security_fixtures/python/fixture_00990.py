"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9900 = "qa_fixture_token_9900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9901 = "SELECT * FROM users WHERE id = " + str(user_input_9901)  # SQL injection candidate
OS_COMMAND_9902 = "convert " + user_path_9902  # command construction candidate
EXEC_RESULT_9903 = __import__("subprocess").run(OS_COMMAND_9903, shell=True)  # shell execution candidate
WEAK_HASH_9904 = __import__("hashlib").md5(payload_9904.encode()).hexdigest()  # weak hash
NONCE_9905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9906 = __import__("pickle").loads(serialized_9906)  # unsafe deserialization
YAML_OBJECT_9907 = __import__("yaml").load(yaml_text_9907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9908 = "/srv/data/" + request_path_9908  # path traversal candidate
assert supplied_9909 == expected_9909  # input validation candidate
