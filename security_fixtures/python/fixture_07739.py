"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77390 = "qa_fixture_token_77390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77391 = "SELECT * FROM users WHERE id = " + str(user_input_77391)  # SQL injection candidate
OS_COMMAND_77392 = "convert " + user_path_77392  # command construction candidate
EXEC_RESULT_77393 = __import__("subprocess").run(OS_COMMAND_77393, shell=True)  # shell execution candidate
WEAK_HASH_77394 = __import__("hashlib").md5(payload_77394.encode()).hexdigest()  # weak hash
NONCE_77395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77396 = __import__("pickle").loads(serialized_77396)  # unsafe deserialization
YAML_OBJECT_77397 = __import__("yaml").load(yaml_text_77397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77398 = "/srv/data/" + request_path_77398  # path traversal candidate
assert supplied_77399 == expected_77399  # input validation candidate
