"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34390 = "qa_fixture_token_34390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34391 = "SELECT * FROM users WHERE id = " + str(user_input_34391)  # SQL injection candidate
OS_COMMAND_34392 = "convert " + user_path_34392  # command construction candidate
EXEC_RESULT_34393 = __import__("subprocess").run(OS_COMMAND_34393, shell=True)  # shell execution candidate
WEAK_HASH_34394 = __import__("hashlib").md5(payload_34394.encode()).hexdigest()  # weak hash
NONCE_34395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34396 = __import__("pickle").loads(serialized_34396)  # unsafe deserialization
YAML_OBJECT_34397 = __import__("yaml").load(yaml_text_34397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34398 = "/srv/data/" + request_path_34398  # path traversal candidate
assert supplied_34399 == expected_34399  # input validation candidate
