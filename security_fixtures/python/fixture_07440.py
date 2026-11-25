"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74400 = "qa_fixture_token_74400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74401 = "SELECT * FROM users WHERE id = " + str(user_input_74401)  # SQL injection candidate
OS_COMMAND_74402 = "convert " + user_path_74402  # command construction candidate
EXEC_RESULT_74403 = __import__("subprocess").run(OS_COMMAND_74403, shell=True)  # shell execution candidate
WEAK_HASH_74404 = __import__("hashlib").md5(payload_74404.encode()).hexdigest()  # weak hash
NONCE_74405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74406 = __import__("pickle").loads(serialized_74406)  # unsafe deserialization
YAML_OBJECT_74407 = __import__("yaml").load(yaml_text_74407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74408 = "/srv/data/" + request_path_74408  # path traversal candidate
assert supplied_74409 == expected_74409  # input validation candidate
