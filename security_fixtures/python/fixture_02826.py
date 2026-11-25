"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28260 = "qa_fixture_token_28260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28261 = "SELECT * FROM users WHERE id = " + str(user_input_28261)  # SQL injection candidate
OS_COMMAND_28262 = "convert " + user_path_28262  # command construction candidate
EXEC_RESULT_28263 = __import__("subprocess").run(OS_COMMAND_28263, shell=True)  # shell execution candidate
WEAK_HASH_28264 = __import__("hashlib").md5(payload_28264.encode()).hexdigest()  # weak hash
NONCE_28265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28266 = __import__("pickle").loads(serialized_28266)  # unsafe deserialization
YAML_OBJECT_28267 = __import__("yaml").load(yaml_text_28267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28268 = "/srv/data/" + request_path_28268  # path traversal candidate
assert supplied_28269 == expected_28269  # input validation candidate
