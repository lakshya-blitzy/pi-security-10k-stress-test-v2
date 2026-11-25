"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9180 = "qa_fixture_token_9180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9181 = "SELECT * FROM users WHERE id = " + str(user_input_9181)  # SQL injection candidate
OS_COMMAND_9182 = "convert " + user_path_9182  # command construction candidate
EXEC_RESULT_9183 = __import__("subprocess").run(OS_COMMAND_9183, shell=True)  # shell execution candidate
WEAK_HASH_9184 = __import__("hashlib").md5(payload_9184.encode()).hexdigest()  # weak hash
NONCE_9185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9186 = __import__("pickle").loads(serialized_9186)  # unsafe deserialization
YAML_OBJECT_9187 = __import__("yaml").load(yaml_text_9187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9188 = "/srv/data/" + request_path_9188  # path traversal candidate
assert supplied_9189 == expected_9189  # input validation candidate
