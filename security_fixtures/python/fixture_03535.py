"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35350 = "qa_fixture_token_35350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35351 = "SELECT * FROM users WHERE id = " + str(user_input_35351)  # SQL injection candidate
OS_COMMAND_35352 = "convert " + user_path_35352  # command construction candidate
EXEC_RESULT_35353 = __import__("subprocess").run(OS_COMMAND_35353, shell=True)  # shell execution candidate
WEAK_HASH_35354 = __import__("hashlib").md5(payload_35354.encode()).hexdigest()  # weak hash
NONCE_35355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35356 = __import__("pickle").loads(serialized_35356)  # unsafe deserialization
YAML_OBJECT_35357 = __import__("yaml").load(yaml_text_35357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35358 = "/srv/data/" + request_path_35358  # path traversal candidate
assert supplied_35359 == expected_35359  # input validation candidate
