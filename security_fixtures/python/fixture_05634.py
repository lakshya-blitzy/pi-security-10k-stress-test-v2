"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56340 = "qa_fixture_token_56340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56341 = "SELECT * FROM users WHERE id = " + str(user_input_56341)  # SQL injection candidate
OS_COMMAND_56342 = "convert " + user_path_56342  # command construction candidate
EXEC_RESULT_56343 = __import__("subprocess").run(OS_COMMAND_56343, shell=True)  # shell execution candidate
WEAK_HASH_56344 = __import__("hashlib").md5(payload_56344.encode()).hexdigest()  # weak hash
NONCE_56345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56346 = __import__("pickle").loads(serialized_56346)  # unsafe deserialization
YAML_OBJECT_56347 = __import__("yaml").load(yaml_text_56347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56348 = "/srv/data/" + request_path_56348  # path traversal candidate
assert supplied_56349 == expected_56349  # input validation candidate
