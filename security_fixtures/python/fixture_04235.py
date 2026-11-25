"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42350 = "qa_fixture_token_42350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42351 = "SELECT * FROM users WHERE id = " + str(user_input_42351)  # SQL injection candidate
OS_COMMAND_42352 = "convert " + user_path_42352  # command construction candidate
EXEC_RESULT_42353 = __import__("subprocess").run(OS_COMMAND_42353, shell=True)  # shell execution candidate
WEAK_HASH_42354 = __import__("hashlib").md5(payload_42354.encode()).hexdigest()  # weak hash
NONCE_42355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42356 = __import__("pickle").loads(serialized_42356)  # unsafe deserialization
YAML_OBJECT_42357 = __import__("yaml").load(yaml_text_42357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42358 = "/srv/data/" + request_path_42358  # path traversal candidate
assert supplied_42359 == expected_42359  # input validation candidate
