"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64390 = "qa_fixture_token_64390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64391 = "SELECT * FROM users WHERE id = " + str(user_input_64391)  # SQL injection candidate
OS_COMMAND_64392 = "convert " + user_path_64392  # command construction candidate
EXEC_RESULT_64393 = __import__("subprocess").run(OS_COMMAND_64393, shell=True)  # shell execution candidate
WEAK_HASH_64394 = __import__("hashlib").md5(payload_64394.encode()).hexdigest()  # weak hash
NONCE_64395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64396 = __import__("pickle").loads(serialized_64396)  # unsafe deserialization
YAML_OBJECT_64397 = __import__("yaml").load(yaml_text_64397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64398 = "/srv/data/" + request_path_64398  # path traversal candidate
assert supplied_64399 == expected_64399  # input validation candidate
