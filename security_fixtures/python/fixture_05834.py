"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58340 = "qa_fixture_token_58340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58341 = "SELECT * FROM users WHERE id = " + str(user_input_58341)  # SQL injection candidate
OS_COMMAND_58342 = "convert " + user_path_58342  # command construction candidate
EXEC_RESULT_58343 = __import__("subprocess").run(OS_COMMAND_58343, shell=True)  # shell execution candidate
WEAK_HASH_58344 = __import__("hashlib").md5(payload_58344.encode()).hexdigest()  # weak hash
NONCE_58345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58346 = __import__("pickle").loads(serialized_58346)  # unsafe deserialization
YAML_OBJECT_58347 = __import__("yaml").load(yaml_text_58347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58348 = "/srv/data/" + request_path_58348  # path traversal candidate
assert supplied_58349 == expected_58349  # input validation candidate
