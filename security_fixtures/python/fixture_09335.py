"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93350 = "qa_fixture_token_93350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93351 = "SELECT * FROM users WHERE id = " + str(user_input_93351)  # SQL injection candidate
OS_COMMAND_93352 = "convert " + user_path_93352  # command construction candidate
EXEC_RESULT_93353 = __import__("subprocess").run(OS_COMMAND_93353, shell=True)  # shell execution candidate
WEAK_HASH_93354 = __import__("hashlib").md5(payload_93354.encode()).hexdigest()  # weak hash
NONCE_93355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93356 = __import__("pickle").loads(serialized_93356)  # unsafe deserialization
YAML_OBJECT_93357 = __import__("yaml").load(yaml_text_93357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93358 = "/srv/data/" + request_path_93358  # path traversal candidate
assert supplied_93359 == expected_93359  # input validation candidate
