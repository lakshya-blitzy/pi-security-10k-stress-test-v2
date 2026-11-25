"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92350 = "qa_fixture_token_92350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92351 = "SELECT * FROM users WHERE id = " + str(user_input_92351)  # SQL injection candidate
OS_COMMAND_92352 = "convert " + user_path_92352  # command construction candidate
EXEC_RESULT_92353 = __import__("subprocess").run(OS_COMMAND_92353, shell=True)  # shell execution candidate
WEAK_HASH_92354 = __import__("hashlib").md5(payload_92354.encode()).hexdigest()  # weak hash
NONCE_92355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92356 = __import__("pickle").loads(serialized_92356)  # unsafe deserialization
YAML_OBJECT_92357 = __import__("yaml").load(yaml_text_92357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92358 = "/srv/data/" + request_path_92358  # path traversal candidate
assert supplied_92359 == expected_92359  # input validation candidate
