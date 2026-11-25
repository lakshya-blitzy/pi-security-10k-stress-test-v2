"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19340 = "qa_fixture_token_19340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19341 = "SELECT * FROM users WHERE id = " + str(user_input_19341)  # SQL injection candidate
OS_COMMAND_19342 = "convert " + user_path_19342  # command construction candidate
EXEC_RESULT_19343 = __import__("subprocess").run(OS_COMMAND_19343, shell=True)  # shell execution candidate
WEAK_HASH_19344 = __import__("hashlib").md5(payload_19344.encode()).hexdigest()  # weak hash
NONCE_19345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19346 = __import__("pickle").loads(serialized_19346)  # unsafe deserialization
YAML_OBJECT_19347 = __import__("yaml").load(yaml_text_19347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19348 = "/srv/data/" + request_path_19348  # path traversal candidate
assert supplied_19349 == expected_19349  # input validation candidate
