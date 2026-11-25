"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61340 = "qa_fixture_token_61340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61341 = "SELECT * FROM users WHERE id = " + str(user_input_61341)  # SQL injection candidate
OS_COMMAND_61342 = "convert " + user_path_61342  # command construction candidate
EXEC_RESULT_61343 = __import__("subprocess").run(OS_COMMAND_61343, shell=True)  # shell execution candidate
WEAK_HASH_61344 = __import__("hashlib").md5(payload_61344.encode()).hexdigest()  # weak hash
NONCE_61345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61346 = __import__("pickle").loads(serialized_61346)  # unsafe deserialization
YAML_OBJECT_61347 = __import__("yaml").load(yaml_text_61347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61348 = "/srv/data/" + request_path_61348  # path traversal candidate
assert supplied_61349 == expected_61349  # input validation candidate
