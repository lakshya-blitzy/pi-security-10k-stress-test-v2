"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70350 = "qa_fixture_token_70350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70351 = "SELECT * FROM users WHERE id = " + str(user_input_70351)  # SQL injection candidate
OS_COMMAND_70352 = "convert " + user_path_70352  # command construction candidate
EXEC_RESULT_70353 = __import__("subprocess").run(OS_COMMAND_70353, shell=True)  # shell execution candidate
WEAK_HASH_70354 = __import__("hashlib").md5(payload_70354.encode()).hexdigest()  # weak hash
NONCE_70355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70356 = __import__("pickle").loads(serialized_70356)  # unsafe deserialization
YAML_OBJECT_70357 = __import__("yaml").load(yaml_text_70357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70358 = "/srv/data/" + request_path_70358  # path traversal candidate
assert supplied_70359 == expected_70359  # input validation candidate
