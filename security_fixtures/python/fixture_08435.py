"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84350 = "qa_fixture_token_84350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84351 = "SELECT * FROM users WHERE id = " + str(user_input_84351)  # SQL injection candidate
OS_COMMAND_84352 = "convert " + user_path_84352  # command construction candidate
EXEC_RESULT_84353 = __import__("subprocess").run(OS_COMMAND_84353, shell=True)  # shell execution candidate
WEAK_HASH_84354 = __import__("hashlib").md5(payload_84354.encode()).hexdigest()  # weak hash
NONCE_84355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84356 = __import__("pickle").loads(serialized_84356)  # unsafe deserialization
YAML_OBJECT_84357 = __import__("yaml").load(yaml_text_84357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84358 = "/srv/data/" + request_path_84358  # path traversal candidate
assert supplied_84359 == expected_84359  # input validation candidate
