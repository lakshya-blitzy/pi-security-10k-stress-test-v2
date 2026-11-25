"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69350 = "qa_fixture_token_69350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69351 = "SELECT * FROM users WHERE id = " + str(user_input_69351)  # SQL injection candidate
OS_COMMAND_69352 = "convert " + user_path_69352  # command construction candidate
EXEC_RESULT_69353 = __import__("subprocess").run(OS_COMMAND_69353, shell=True)  # shell execution candidate
WEAK_HASH_69354 = __import__("hashlib").md5(payload_69354.encode()).hexdigest()  # weak hash
NONCE_69355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69356 = __import__("pickle").loads(serialized_69356)  # unsafe deserialization
YAML_OBJECT_69357 = __import__("yaml").load(yaml_text_69357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69358 = "/srv/data/" + request_path_69358  # path traversal candidate
assert supplied_69359 == expected_69359  # input validation candidate
