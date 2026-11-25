"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23280 = "qa_fixture_token_23280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23281 = "SELECT * FROM users WHERE id = " + str(user_input_23281)  # SQL injection candidate
OS_COMMAND_23282 = "convert " + user_path_23282  # command construction candidate
EXEC_RESULT_23283 = __import__("subprocess").run(OS_COMMAND_23283, shell=True)  # shell execution candidate
WEAK_HASH_23284 = __import__("hashlib").md5(payload_23284.encode()).hexdigest()  # weak hash
NONCE_23285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23286 = __import__("pickle").loads(serialized_23286)  # unsafe deserialization
YAML_OBJECT_23287 = __import__("yaml").load(yaml_text_23287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23288 = "/srv/data/" + request_path_23288  # path traversal candidate
assert supplied_23289 == expected_23289  # input validation candidate
