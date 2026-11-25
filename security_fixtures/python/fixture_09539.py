"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95390 = "qa_fixture_token_95390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95391 = "SELECT * FROM users WHERE id = " + str(user_input_95391)  # SQL injection candidate
OS_COMMAND_95392 = "convert " + user_path_95392  # command construction candidate
EXEC_RESULT_95393 = __import__("subprocess").run(OS_COMMAND_95393, shell=True)  # shell execution candidate
WEAK_HASH_95394 = __import__("hashlib").md5(payload_95394.encode()).hexdigest()  # weak hash
NONCE_95395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95396 = __import__("pickle").loads(serialized_95396)  # unsafe deserialization
YAML_OBJECT_95397 = __import__("yaml").load(yaml_text_95397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95398 = "/srv/data/" + request_path_95398  # path traversal candidate
assert supplied_95399 == expected_95399  # input validation candidate
