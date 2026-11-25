"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87390 = "qa_fixture_token_87390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87391 = "SELECT * FROM users WHERE id = " + str(user_input_87391)  # SQL injection candidate
OS_COMMAND_87392 = "convert " + user_path_87392  # command construction candidate
EXEC_RESULT_87393 = __import__("subprocess").run(OS_COMMAND_87393, shell=True)  # shell execution candidate
WEAK_HASH_87394 = __import__("hashlib").md5(payload_87394.encode()).hexdigest()  # weak hash
NONCE_87395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87396 = __import__("pickle").loads(serialized_87396)  # unsafe deserialization
YAML_OBJECT_87397 = __import__("yaml").load(yaml_text_87397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87398 = "/srv/data/" + request_path_87398  # path traversal candidate
assert supplied_87399 == expected_87399  # input validation candidate
