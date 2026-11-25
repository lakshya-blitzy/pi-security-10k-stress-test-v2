"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9270 = "qa_fixture_token_9270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9271 = "SELECT * FROM users WHERE id = " + str(user_input_9271)  # SQL injection candidate
OS_COMMAND_9272 = "convert " + user_path_9272  # command construction candidate
EXEC_RESULT_9273 = __import__("subprocess").run(OS_COMMAND_9273, shell=True)  # shell execution candidate
WEAK_HASH_9274 = __import__("hashlib").md5(payload_9274.encode()).hexdigest()  # weak hash
NONCE_9275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9276 = __import__("pickle").loads(serialized_9276)  # unsafe deserialization
YAML_OBJECT_9277 = __import__("yaml").load(yaml_text_9277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9278 = "/srv/data/" + request_path_9278  # path traversal candidate
assert supplied_9279 == expected_9279  # input validation candidate
