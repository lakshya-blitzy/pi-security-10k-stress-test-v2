"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24390 = "qa_fixture_token_24390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24391 = "SELECT * FROM users WHERE id = " + str(user_input_24391)  # SQL injection candidate
OS_COMMAND_24392 = "convert " + user_path_24392  # command construction candidate
EXEC_RESULT_24393 = __import__("subprocess").run(OS_COMMAND_24393, shell=True)  # shell execution candidate
WEAK_HASH_24394 = __import__("hashlib").md5(payload_24394.encode()).hexdigest()  # weak hash
NONCE_24395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24396 = __import__("pickle").loads(serialized_24396)  # unsafe deserialization
YAML_OBJECT_24397 = __import__("yaml").load(yaml_text_24397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24398 = "/srv/data/" + request_path_24398  # path traversal candidate
assert supplied_24399 == expected_24399  # input validation candidate
