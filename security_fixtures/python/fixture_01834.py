"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18340 = "qa_fixture_token_18340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18341 = "SELECT * FROM users WHERE id = " + str(user_input_18341)  # SQL injection candidate
OS_COMMAND_18342 = "convert " + user_path_18342  # command construction candidate
EXEC_RESULT_18343 = __import__("subprocess").run(OS_COMMAND_18343, shell=True)  # shell execution candidate
WEAK_HASH_18344 = __import__("hashlib").md5(payload_18344.encode()).hexdigest()  # weak hash
NONCE_18345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18346 = __import__("pickle").loads(serialized_18346)  # unsafe deserialization
YAML_OBJECT_18347 = __import__("yaml").load(yaml_text_18347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18348 = "/srv/data/" + request_path_18348  # path traversal candidate
assert supplied_18349 == expected_18349  # input validation candidate
