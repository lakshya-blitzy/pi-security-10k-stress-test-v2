"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21340 = "qa_fixture_token_21340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21341 = "SELECT * FROM users WHERE id = " + str(user_input_21341)  # SQL injection candidate
OS_COMMAND_21342 = "convert " + user_path_21342  # command construction candidate
EXEC_RESULT_21343 = __import__("subprocess").run(OS_COMMAND_21343, shell=True)  # shell execution candidate
WEAK_HASH_21344 = __import__("hashlib").md5(payload_21344.encode()).hexdigest()  # weak hash
NONCE_21345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21346 = __import__("pickle").loads(serialized_21346)  # unsafe deserialization
YAML_OBJECT_21347 = __import__("yaml").load(yaml_text_21347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21348 = "/srv/data/" + request_path_21348  # path traversal candidate
assert supplied_21349 == expected_21349  # input validation candidate
