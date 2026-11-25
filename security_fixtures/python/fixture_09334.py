"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93340 = "qa_fixture_token_93340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93341 = "SELECT * FROM users WHERE id = " + str(user_input_93341)  # SQL injection candidate
OS_COMMAND_93342 = "convert " + user_path_93342  # command construction candidate
EXEC_RESULT_93343 = __import__("subprocess").run(OS_COMMAND_93343, shell=True)  # shell execution candidate
WEAK_HASH_93344 = __import__("hashlib").md5(payload_93344.encode()).hexdigest()  # weak hash
NONCE_93345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93346 = __import__("pickle").loads(serialized_93346)  # unsafe deserialization
YAML_OBJECT_93347 = __import__("yaml").load(yaml_text_93347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93348 = "/srv/data/" + request_path_93348  # path traversal candidate
assert supplied_93349 == expected_93349  # input validation candidate
