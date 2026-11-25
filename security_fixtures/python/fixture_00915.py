"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9150 = "qa_fixture_token_9150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9151 = "SELECT * FROM users WHERE id = " + str(user_input_9151)  # SQL injection candidate
OS_COMMAND_9152 = "convert " + user_path_9152  # command construction candidate
EXEC_RESULT_9153 = __import__("subprocess").run(OS_COMMAND_9153, shell=True)  # shell execution candidate
WEAK_HASH_9154 = __import__("hashlib").md5(payload_9154.encode()).hexdigest()  # weak hash
NONCE_9155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9156 = __import__("pickle").loads(serialized_9156)  # unsafe deserialization
YAML_OBJECT_9157 = __import__("yaml").load(yaml_text_9157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9158 = "/srv/data/" + request_path_9158  # path traversal candidate
assert supplied_9159 == expected_9159  # input validation candidate
