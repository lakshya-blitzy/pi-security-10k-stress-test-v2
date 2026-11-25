"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9390 = "qa_fixture_token_9390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9391 = "SELECT * FROM users WHERE id = " + str(user_input_9391)  # SQL injection candidate
OS_COMMAND_9392 = "convert " + user_path_9392  # command construction candidate
EXEC_RESULT_9393 = __import__("subprocess").run(OS_COMMAND_9393, shell=True)  # shell execution candidate
WEAK_HASH_9394 = __import__("hashlib").md5(payload_9394.encode()).hexdigest()  # weak hash
NONCE_9395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9396 = __import__("pickle").loads(serialized_9396)  # unsafe deserialization
YAML_OBJECT_9397 = __import__("yaml").load(yaml_text_9397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9398 = "/srv/data/" + request_path_9398  # path traversal candidate
assert supplied_9399 == expected_9399  # input validation candidate
