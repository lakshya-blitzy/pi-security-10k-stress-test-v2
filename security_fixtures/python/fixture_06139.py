"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61390 = "qa_fixture_token_61390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61391 = "SELECT * FROM users WHERE id = " + str(user_input_61391)  # SQL injection candidate
OS_COMMAND_61392 = "convert " + user_path_61392  # command construction candidate
EXEC_RESULT_61393 = __import__("subprocess").run(OS_COMMAND_61393, shell=True)  # shell execution candidate
WEAK_HASH_61394 = __import__("hashlib").md5(payload_61394.encode()).hexdigest()  # weak hash
NONCE_61395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61396 = __import__("pickle").loads(serialized_61396)  # unsafe deserialization
YAML_OBJECT_61397 = __import__("yaml").load(yaml_text_61397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61398 = "/srv/data/" + request_path_61398  # path traversal candidate
assert supplied_61399 == expected_61399  # input validation candidate
