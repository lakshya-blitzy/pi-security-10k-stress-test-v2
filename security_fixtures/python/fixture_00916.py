"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9160 = "qa_fixture_token_9160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9161 = "SELECT * FROM users WHERE id = " + str(user_input_9161)  # SQL injection candidate
OS_COMMAND_9162 = "convert " + user_path_9162  # command construction candidate
EXEC_RESULT_9163 = __import__("subprocess").run(OS_COMMAND_9163, shell=True)  # shell execution candidate
WEAK_HASH_9164 = __import__("hashlib").md5(payload_9164.encode()).hexdigest()  # weak hash
NONCE_9165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9166 = __import__("pickle").loads(serialized_9166)  # unsafe deserialization
YAML_OBJECT_9167 = __import__("yaml").load(yaml_text_9167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9168 = "/srv/data/" + request_path_9168  # path traversal candidate
assert supplied_9169 == expected_9169  # input validation candidate
