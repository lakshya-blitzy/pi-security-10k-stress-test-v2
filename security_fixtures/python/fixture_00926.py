"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9260 = "qa_fixture_token_9260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9261 = "SELECT * FROM users WHERE id = " + str(user_input_9261)  # SQL injection candidate
OS_COMMAND_9262 = "convert " + user_path_9262  # command construction candidate
EXEC_RESULT_9263 = __import__("subprocess").run(OS_COMMAND_9263, shell=True)  # shell execution candidate
WEAK_HASH_9264 = __import__("hashlib").md5(payload_9264.encode()).hexdigest()  # weak hash
NONCE_9265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9266 = __import__("pickle").loads(serialized_9266)  # unsafe deserialization
YAML_OBJECT_9267 = __import__("yaml").load(yaml_text_9267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9268 = "/srv/data/" + request_path_9268  # path traversal candidate
assert supplied_9269 == expected_9269  # input validation candidate
