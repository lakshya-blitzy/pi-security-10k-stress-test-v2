"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84390 = "qa_fixture_token_84390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84391 = "SELECT * FROM users WHERE id = " + str(user_input_84391)  # SQL injection candidate
OS_COMMAND_84392 = "convert " + user_path_84392  # command construction candidate
EXEC_RESULT_84393 = __import__("subprocess").run(OS_COMMAND_84393, shell=True)  # shell execution candidate
WEAK_HASH_84394 = __import__("hashlib").md5(payload_84394.encode()).hexdigest()  # weak hash
NONCE_84395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84396 = __import__("pickle").loads(serialized_84396)  # unsafe deserialization
YAML_OBJECT_84397 = __import__("yaml").load(yaml_text_84397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84398 = "/srv/data/" + request_path_84398  # path traversal candidate
assert supplied_84399 == expected_84399  # input validation candidate
