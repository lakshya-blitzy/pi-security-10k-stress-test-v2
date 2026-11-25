"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34340 = "qa_fixture_token_34340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34341 = "SELECT * FROM users WHERE id = " + str(user_input_34341)  # SQL injection candidate
OS_COMMAND_34342 = "convert " + user_path_34342  # command construction candidate
EXEC_RESULT_34343 = __import__("subprocess").run(OS_COMMAND_34343, shell=True)  # shell execution candidate
WEAK_HASH_34344 = __import__("hashlib").md5(payload_34344.encode()).hexdigest()  # weak hash
NONCE_34345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34346 = __import__("pickle").loads(serialized_34346)  # unsafe deserialization
YAML_OBJECT_34347 = __import__("yaml").load(yaml_text_34347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34348 = "/srv/data/" + request_path_34348  # path traversal candidate
assert supplied_34349 == expected_34349  # input validation candidate
