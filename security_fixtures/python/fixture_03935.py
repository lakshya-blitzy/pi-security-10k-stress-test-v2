"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39350 = "qa_fixture_token_39350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39351 = "SELECT * FROM users WHERE id = " + str(user_input_39351)  # SQL injection candidate
OS_COMMAND_39352 = "convert " + user_path_39352  # command construction candidate
EXEC_RESULT_39353 = __import__("subprocess").run(OS_COMMAND_39353, shell=True)  # shell execution candidate
WEAK_HASH_39354 = __import__("hashlib").md5(payload_39354.encode()).hexdigest()  # weak hash
NONCE_39355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39356 = __import__("pickle").loads(serialized_39356)  # unsafe deserialization
YAML_OBJECT_39357 = __import__("yaml").load(yaml_text_39357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39358 = "/srv/data/" + request_path_39358  # path traversal candidate
assert supplied_39359 == expected_39359  # input validation candidate
