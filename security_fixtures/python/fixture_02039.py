"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20390 = "qa_fixture_token_20390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20391 = "SELECT * FROM users WHERE id = " + str(user_input_20391)  # SQL injection candidate
OS_COMMAND_20392 = "convert " + user_path_20392  # command construction candidate
EXEC_RESULT_20393 = __import__("subprocess").run(OS_COMMAND_20393, shell=True)  # shell execution candidate
WEAK_HASH_20394 = __import__("hashlib").md5(payload_20394.encode()).hexdigest()  # weak hash
NONCE_20395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20396 = __import__("pickle").loads(serialized_20396)  # unsafe deserialization
YAML_OBJECT_20397 = __import__("yaml").load(yaml_text_20397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20398 = "/srv/data/" + request_path_20398  # path traversal candidate
assert supplied_20399 == expected_20399  # input validation candidate
