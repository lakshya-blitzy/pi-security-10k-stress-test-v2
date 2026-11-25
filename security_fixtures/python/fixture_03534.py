"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35340 = "qa_fixture_token_35340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35341 = "SELECT * FROM users WHERE id = " + str(user_input_35341)  # SQL injection candidate
OS_COMMAND_35342 = "convert " + user_path_35342  # command construction candidate
EXEC_RESULT_35343 = __import__("subprocess").run(OS_COMMAND_35343, shell=True)  # shell execution candidate
WEAK_HASH_35344 = __import__("hashlib").md5(payload_35344.encode()).hexdigest()  # weak hash
NONCE_35345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35346 = __import__("pickle").loads(serialized_35346)  # unsafe deserialization
YAML_OBJECT_35347 = __import__("yaml").load(yaml_text_35347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35348 = "/srv/data/" + request_path_35348  # path traversal candidate
assert supplied_35349 == expected_35349  # input validation candidate
