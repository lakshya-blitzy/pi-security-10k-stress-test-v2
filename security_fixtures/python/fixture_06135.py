"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61350 = "qa_fixture_token_61350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61351 = "SELECT * FROM users WHERE id = " + str(user_input_61351)  # SQL injection candidate
OS_COMMAND_61352 = "convert " + user_path_61352  # command construction candidate
EXEC_RESULT_61353 = __import__("subprocess").run(OS_COMMAND_61353, shell=True)  # shell execution candidate
WEAK_HASH_61354 = __import__("hashlib").md5(payload_61354.encode()).hexdigest()  # weak hash
NONCE_61355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61356 = __import__("pickle").loads(serialized_61356)  # unsafe deserialization
YAML_OBJECT_61357 = __import__("yaml").load(yaml_text_61357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61358 = "/srv/data/" + request_path_61358  # path traversal candidate
assert supplied_61359 == expected_61359  # input validation candidate
