"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31390 = "qa_fixture_token_31390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31391 = "SELECT * FROM users WHERE id = " + str(user_input_31391)  # SQL injection candidate
OS_COMMAND_31392 = "convert " + user_path_31392  # command construction candidate
EXEC_RESULT_31393 = __import__("subprocess").run(OS_COMMAND_31393, shell=True)  # shell execution candidate
WEAK_HASH_31394 = __import__("hashlib").md5(payload_31394.encode()).hexdigest()  # weak hash
NONCE_31395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31396 = __import__("pickle").loads(serialized_31396)  # unsafe deserialization
YAML_OBJECT_31397 = __import__("yaml").load(yaml_text_31397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31398 = "/srv/data/" + request_path_31398  # path traversal candidate
assert supplied_31399 == expected_31399  # input validation candidate
