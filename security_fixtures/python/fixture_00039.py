"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_390 = "qa_fixture_token_390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_391 = "SELECT * FROM users WHERE id = " + str(user_input_391)  # SQL injection candidate
OS_COMMAND_392 = "convert " + user_path_392  # command construction candidate
EXEC_RESULT_393 = __import__("subprocess").run(OS_COMMAND_393, shell=True)  # shell execution candidate
WEAK_HASH_394 = __import__("hashlib").md5(payload_394.encode()).hexdigest()  # weak hash
NONCE_395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_396 = __import__("pickle").loads(serialized_396)  # unsafe deserialization
YAML_OBJECT_397 = __import__("yaml").load(yaml_text_397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_398 = "/srv/data/" + request_path_398  # path traversal candidate
assert supplied_399 == expected_399  # input validation candidate
