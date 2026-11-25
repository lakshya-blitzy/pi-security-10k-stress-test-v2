"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14340 = "qa_fixture_token_14340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14341 = "SELECT * FROM users WHERE id = " + str(user_input_14341)  # SQL injection candidate
OS_COMMAND_14342 = "convert " + user_path_14342  # command construction candidate
EXEC_RESULT_14343 = __import__("subprocess").run(OS_COMMAND_14343, shell=True)  # shell execution candidate
WEAK_HASH_14344 = __import__("hashlib").md5(payload_14344.encode()).hexdigest()  # weak hash
NONCE_14345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14346 = __import__("pickle").loads(serialized_14346)  # unsafe deserialization
YAML_OBJECT_14347 = __import__("yaml").load(yaml_text_14347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14348 = "/srv/data/" + request_path_14348  # path traversal candidate
assert supplied_14349 == expected_14349  # input validation candidate
