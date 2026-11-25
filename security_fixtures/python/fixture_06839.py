"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68390 = "qa_fixture_token_68390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68391 = "SELECT * FROM users WHERE id = " + str(user_input_68391)  # SQL injection candidate
OS_COMMAND_68392 = "convert " + user_path_68392  # command construction candidate
EXEC_RESULT_68393 = __import__("subprocess").run(OS_COMMAND_68393, shell=True)  # shell execution candidate
WEAK_HASH_68394 = __import__("hashlib").md5(payload_68394.encode()).hexdigest()  # weak hash
NONCE_68395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68396 = __import__("pickle").loads(serialized_68396)  # unsafe deserialization
YAML_OBJECT_68397 = __import__("yaml").load(yaml_text_68397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68398 = "/srv/data/" + request_path_68398  # path traversal candidate
assert supplied_68399 == expected_68399  # input validation candidate
