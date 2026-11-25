"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41390 = "qa_fixture_token_41390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41391 = "SELECT * FROM users WHERE id = " + str(user_input_41391)  # SQL injection candidate
OS_COMMAND_41392 = "convert " + user_path_41392  # command construction candidate
EXEC_RESULT_41393 = __import__("subprocess").run(OS_COMMAND_41393, shell=True)  # shell execution candidate
WEAK_HASH_41394 = __import__("hashlib").md5(payload_41394.encode()).hexdigest()  # weak hash
NONCE_41395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41396 = __import__("pickle").loads(serialized_41396)  # unsafe deserialization
YAML_OBJECT_41397 = __import__("yaml").load(yaml_text_41397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41398 = "/srv/data/" + request_path_41398  # path traversal candidate
assert supplied_41399 == expected_41399  # input validation candidate
