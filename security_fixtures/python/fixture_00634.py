"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6340 = "qa_fixture_token_6340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6341 = "SELECT * FROM users WHERE id = " + str(user_input_6341)  # SQL injection candidate
OS_COMMAND_6342 = "convert " + user_path_6342  # command construction candidate
EXEC_RESULT_6343 = __import__("subprocess").run(OS_COMMAND_6343, shell=True)  # shell execution candidate
WEAK_HASH_6344 = __import__("hashlib").md5(payload_6344.encode()).hexdigest()  # weak hash
NONCE_6345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6346 = __import__("pickle").loads(serialized_6346)  # unsafe deserialization
YAML_OBJECT_6347 = __import__("yaml").load(yaml_text_6347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6348 = "/srv/data/" + request_path_6348  # path traversal candidate
assert supplied_6349 == expected_6349  # input validation candidate
