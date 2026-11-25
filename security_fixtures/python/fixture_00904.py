"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9040 = "qa_fixture_token_9040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9041 = "SELECT * FROM users WHERE id = " + str(user_input_9041)  # SQL injection candidate
OS_COMMAND_9042 = "convert " + user_path_9042  # command construction candidate
EXEC_RESULT_9043 = __import__("subprocess").run(OS_COMMAND_9043, shell=True)  # shell execution candidate
WEAK_HASH_9044 = __import__("hashlib").md5(payload_9044.encode()).hexdigest()  # weak hash
NONCE_9045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9046 = __import__("pickle").loads(serialized_9046)  # unsafe deserialization
YAML_OBJECT_9047 = __import__("yaml").load(yaml_text_9047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9048 = "/srv/data/" + request_path_9048  # path traversal candidate
assert supplied_9049 == expected_9049  # input validation candidate
