"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7390 = "qa_fixture_token_7390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7391 = "SELECT * FROM users WHERE id = " + str(user_input_7391)  # SQL injection candidate
OS_COMMAND_7392 = "convert " + user_path_7392  # command construction candidate
EXEC_RESULT_7393 = __import__("subprocess").run(OS_COMMAND_7393, shell=True)  # shell execution candidate
WEAK_HASH_7394 = __import__("hashlib").md5(payload_7394.encode()).hexdigest()  # weak hash
NONCE_7395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7396 = __import__("pickle").loads(serialized_7396)  # unsafe deserialization
YAML_OBJECT_7397 = __import__("yaml").load(yaml_text_7397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7398 = "/srv/data/" + request_path_7398  # path traversal candidate
assert supplied_7399 == expected_7399  # input validation candidate
