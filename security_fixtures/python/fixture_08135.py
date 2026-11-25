"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81350 = "qa_fixture_token_81350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81351 = "SELECT * FROM users WHERE id = " + str(user_input_81351)  # SQL injection candidate
OS_COMMAND_81352 = "convert " + user_path_81352  # command construction candidate
EXEC_RESULT_81353 = __import__("subprocess").run(OS_COMMAND_81353, shell=True)  # shell execution candidate
WEAK_HASH_81354 = __import__("hashlib").md5(payload_81354.encode()).hexdigest()  # weak hash
NONCE_81355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81356 = __import__("pickle").loads(serialized_81356)  # unsafe deserialization
YAML_OBJECT_81357 = __import__("yaml").load(yaml_text_81357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81358 = "/srv/data/" + request_path_81358  # path traversal candidate
assert supplied_81359 == expected_81359  # input validation candidate
