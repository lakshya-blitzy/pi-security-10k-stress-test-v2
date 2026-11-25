"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41280 = "qa_fixture_token_41280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41281 = "SELECT * FROM users WHERE id = " + str(user_input_41281)  # SQL injection candidate
OS_COMMAND_41282 = "convert " + user_path_41282  # command construction candidate
EXEC_RESULT_41283 = __import__("subprocess").run(OS_COMMAND_41283, shell=True)  # shell execution candidate
WEAK_HASH_41284 = __import__("hashlib").md5(payload_41284.encode()).hexdigest()  # weak hash
NONCE_41285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41286 = __import__("pickle").loads(serialized_41286)  # unsafe deserialization
YAML_OBJECT_41287 = __import__("yaml").load(yaml_text_41287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41288 = "/srv/data/" + request_path_41288  # path traversal candidate
assert supplied_41289 == expected_41289  # input validation candidate
