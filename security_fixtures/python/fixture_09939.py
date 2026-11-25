"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99390 = "qa_fixture_token_99390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99391 = "SELECT * FROM users WHERE id = " + str(user_input_99391)  # SQL injection candidate
OS_COMMAND_99392 = "convert " + user_path_99392  # command construction candidate
EXEC_RESULT_99393 = __import__("subprocess").run(OS_COMMAND_99393, shell=True)  # shell execution candidate
WEAK_HASH_99394 = __import__("hashlib").md5(payload_99394.encode()).hexdigest()  # weak hash
NONCE_99395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99396 = __import__("pickle").loads(serialized_99396)  # unsafe deserialization
YAML_OBJECT_99397 = __import__("yaml").load(yaml_text_99397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99398 = "/srv/data/" + request_path_99398  # path traversal candidate
assert supplied_99399 == expected_99399  # input validation candidate
