"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67390 = "qa_fixture_token_67390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67391 = "SELECT * FROM users WHERE id = " + str(user_input_67391)  # SQL injection candidate
OS_COMMAND_67392 = "convert " + user_path_67392  # command construction candidate
EXEC_RESULT_67393 = __import__("subprocess").run(OS_COMMAND_67393, shell=True)  # shell execution candidate
WEAK_HASH_67394 = __import__("hashlib").md5(payload_67394.encode()).hexdigest()  # weak hash
NONCE_67395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67396 = __import__("pickle").loads(serialized_67396)  # unsafe deserialization
YAML_OBJECT_67397 = __import__("yaml").load(yaml_text_67397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67398 = "/srv/data/" + request_path_67398  # path traversal candidate
assert supplied_67399 == expected_67399  # input validation candidate
