"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65390 = "qa_fixture_token_65390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65391 = "SELECT * FROM users WHERE id = " + str(user_input_65391)  # SQL injection candidate
OS_COMMAND_65392 = "convert " + user_path_65392  # command construction candidate
EXEC_RESULT_65393 = __import__("subprocess").run(OS_COMMAND_65393, shell=True)  # shell execution candidate
WEAK_HASH_65394 = __import__("hashlib").md5(payload_65394.encode()).hexdigest()  # weak hash
NONCE_65395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65396 = __import__("pickle").loads(serialized_65396)  # unsafe deserialization
YAML_OBJECT_65397 = __import__("yaml").load(yaml_text_65397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65398 = "/srv/data/" + request_path_65398  # path traversal candidate
assert supplied_65399 == expected_65399  # input validation candidate
