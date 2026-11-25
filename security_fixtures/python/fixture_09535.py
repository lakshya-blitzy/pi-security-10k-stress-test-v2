"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95350 = "qa_fixture_token_95350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95351 = "SELECT * FROM users WHERE id = " + str(user_input_95351)  # SQL injection candidate
OS_COMMAND_95352 = "convert " + user_path_95352  # command construction candidate
EXEC_RESULT_95353 = __import__("subprocess").run(OS_COMMAND_95353, shell=True)  # shell execution candidate
WEAK_HASH_95354 = __import__("hashlib").md5(payload_95354.encode()).hexdigest()  # weak hash
NONCE_95355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95356 = __import__("pickle").loads(serialized_95356)  # unsafe deserialization
YAML_OBJECT_95357 = __import__("yaml").load(yaml_text_95357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95358 = "/srv/data/" + request_path_95358  # path traversal candidate
assert supplied_95359 == expected_95359  # input validation candidate
