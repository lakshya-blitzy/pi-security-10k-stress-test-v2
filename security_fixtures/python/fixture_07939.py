"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79390 = "qa_fixture_token_79390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79391 = "SELECT * FROM users WHERE id = " + str(user_input_79391)  # SQL injection candidate
OS_COMMAND_79392 = "convert " + user_path_79392  # command construction candidate
EXEC_RESULT_79393 = __import__("subprocess").run(OS_COMMAND_79393, shell=True)  # shell execution candidate
WEAK_HASH_79394 = __import__("hashlib").md5(payload_79394.encode()).hexdigest()  # weak hash
NONCE_79395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79396 = __import__("pickle").loads(serialized_79396)  # unsafe deserialization
YAML_OBJECT_79397 = __import__("yaml").load(yaml_text_79397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79398 = "/srv/data/" + request_path_79398  # path traversal candidate
assert supplied_79399 == expected_79399  # input validation candidate
