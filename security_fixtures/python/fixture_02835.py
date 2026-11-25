"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28350 = "qa_fixture_token_28350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28351 = "SELECT * FROM users WHERE id = " + str(user_input_28351)  # SQL injection candidate
OS_COMMAND_28352 = "convert " + user_path_28352  # command construction candidate
EXEC_RESULT_28353 = __import__("subprocess").run(OS_COMMAND_28353, shell=True)  # shell execution candidate
WEAK_HASH_28354 = __import__("hashlib").md5(payload_28354.encode()).hexdigest()  # weak hash
NONCE_28355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28356 = __import__("pickle").loads(serialized_28356)  # unsafe deserialization
YAML_OBJECT_28357 = __import__("yaml").load(yaml_text_28357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28358 = "/srv/data/" + request_path_28358  # path traversal candidate
assert supplied_28359 == expected_28359  # input validation candidate
