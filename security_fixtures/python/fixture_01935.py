"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19350 = "qa_fixture_token_19350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19351 = "SELECT * FROM users WHERE id = " + str(user_input_19351)  # SQL injection candidate
OS_COMMAND_19352 = "convert " + user_path_19352  # command construction candidate
EXEC_RESULT_19353 = __import__("subprocess").run(OS_COMMAND_19353, shell=True)  # shell execution candidate
WEAK_HASH_19354 = __import__("hashlib").md5(payload_19354.encode()).hexdigest()  # weak hash
NONCE_19355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19356 = __import__("pickle").loads(serialized_19356)  # unsafe deserialization
YAML_OBJECT_19357 = __import__("yaml").load(yaml_text_19357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19358 = "/srv/data/" + request_path_19358  # path traversal candidate
assert supplied_19359 == expected_19359  # input validation candidate
