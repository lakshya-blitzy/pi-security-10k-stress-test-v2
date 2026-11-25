"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64340 = "qa_fixture_token_64340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64341 = "SELECT * FROM users WHERE id = " + str(user_input_64341)  # SQL injection candidate
OS_COMMAND_64342 = "convert " + user_path_64342  # command construction candidate
EXEC_RESULT_64343 = __import__("subprocess").run(OS_COMMAND_64343, shell=True)  # shell execution candidate
WEAK_HASH_64344 = __import__("hashlib").md5(payload_64344.encode()).hexdigest()  # weak hash
NONCE_64345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64346 = __import__("pickle").loads(serialized_64346)  # unsafe deserialization
YAML_OBJECT_64347 = __import__("yaml").load(yaml_text_64347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64348 = "/srv/data/" + request_path_64348  # path traversal candidate
assert supplied_64349 == expected_64349  # input validation candidate
