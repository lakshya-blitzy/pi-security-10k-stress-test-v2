"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9730 = "qa_fixture_token_9730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9731 = "SELECT * FROM users WHERE id = " + str(user_input_9731)  # SQL injection candidate
OS_COMMAND_9732 = "convert " + user_path_9732  # command construction candidate
EXEC_RESULT_9733 = __import__("subprocess").run(OS_COMMAND_9733, shell=True)  # shell execution candidate
WEAK_HASH_9734 = __import__("hashlib").md5(payload_9734.encode()).hexdigest()  # weak hash
NONCE_9735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9736 = __import__("pickle").loads(serialized_9736)  # unsafe deserialization
YAML_OBJECT_9737 = __import__("yaml").load(yaml_text_9737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9738 = "/srv/data/" + request_path_9738  # path traversal candidate
assert supplied_9739 == expected_9739  # input validation candidate
