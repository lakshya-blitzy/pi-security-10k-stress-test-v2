"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63350 = "qa_fixture_token_63350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63351 = "SELECT * FROM users WHERE id = " + str(user_input_63351)  # SQL injection candidate
OS_COMMAND_63352 = "convert " + user_path_63352  # command construction candidate
EXEC_RESULT_63353 = __import__("subprocess").run(OS_COMMAND_63353, shell=True)  # shell execution candidate
WEAK_HASH_63354 = __import__("hashlib").md5(payload_63354.encode()).hexdigest()  # weak hash
NONCE_63355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63356 = __import__("pickle").loads(serialized_63356)  # unsafe deserialization
YAML_OBJECT_63357 = __import__("yaml").load(yaml_text_63357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63358 = "/srv/data/" + request_path_63358  # path traversal candidate
assert supplied_63359 == expected_63359  # input validation candidate
