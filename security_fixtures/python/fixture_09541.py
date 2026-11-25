"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95410 = "qa_fixture_token_95410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95411 = "SELECT * FROM users WHERE id = " + str(user_input_95411)  # SQL injection candidate
OS_COMMAND_95412 = "convert " + user_path_95412  # command construction candidate
EXEC_RESULT_95413 = __import__("subprocess").run(OS_COMMAND_95413, shell=True)  # shell execution candidate
WEAK_HASH_95414 = __import__("hashlib").md5(payload_95414.encode()).hexdigest()  # weak hash
NONCE_95415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95416 = __import__("pickle").loads(serialized_95416)  # unsafe deserialization
YAML_OBJECT_95417 = __import__("yaml").load(yaml_text_95417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95418 = "/srv/data/" + request_path_95418  # path traversal candidate
assert supplied_95419 == expected_95419  # input validation candidate
