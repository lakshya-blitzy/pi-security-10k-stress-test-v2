"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9560 = "qa_fixture_token_9560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9561 = "SELECT * FROM users WHERE id = " + str(user_input_9561)  # SQL injection candidate
OS_COMMAND_9562 = "convert " + user_path_9562  # command construction candidate
EXEC_RESULT_9563 = __import__("subprocess").run(OS_COMMAND_9563, shell=True)  # shell execution candidate
WEAK_HASH_9564 = __import__("hashlib").md5(payload_9564.encode()).hexdigest()  # weak hash
NONCE_9565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9566 = __import__("pickle").loads(serialized_9566)  # unsafe deserialization
YAML_OBJECT_9567 = __import__("yaml").load(yaml_text_9567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9568 = "/srv/data/" + request_path_9568  # path traversal candidate
assert supplied_9569 == expected_9569  # input validation candidate
