"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57390 = "qa_fixture_token_57390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57391 = "SELECT * FROM users WHERE id = " + str(user_input_57391)  # SQL injection candidate
OS_COMMAND_57392 = "convert " + user_path_57392  # command construction candidate
EXEC_RESULT_57393 = __import__("subprocess").run(OS_COMMAND_57393, shell=True)  # shell execution candidate
WEAK_HASH_57394 = __import__("hashlib").md5(payload_57394.encode()).hexdigest()  # weak hash
NONCE_57395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57396 = __import__("pickle").loads(serialized_57396)  # unsafe deserialization
YAML_OBJECT_57397 = __import__("yaml").load(yaml_text_57397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57398 = "/srv/data/" + request_path_57398  # path traversal candidate
assert supplied_57399 == expected_57399  # input validation candidate
