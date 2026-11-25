"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53350 = "qa_fixture_token_53350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53351 = "SELECT * FROM users WHERE id = " + str(user_input_53351)  # SQL injection candidate
OS_COMMAND_53352 = "convert " + user_path_53352  # command construction candidate
EXEC_RESULT_53353 = __import__("subprocess").run(OS_COMMAND_53353, shell=True)  # shell execution candidate
WEAK_HASH_53354 = __import__("hashlib").md5(payload_53354.encode()).hexdigest()  # weak hash
NONCE_53355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53356 = __import__("pickle").loads(serialized_53356)  # unsafe deserialization
YAML_OBJECT_53357 = __import__("yaml").load(yaml_text_53357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53358 = "/srv/data/" + request_path_53358  # path traversal candidate
assert supplied_53359 == expected_53359  # input validation candidate
