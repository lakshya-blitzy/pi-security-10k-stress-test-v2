"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54390 = "qa_fixture_token_54390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54391 = "SELECT * FROM users WHERE id = " + str(user_input_54391)  # SQL injection candidate
OS_COMMAND_54392 = "convert " + user_path_54392  # command construction candidate
EXEC_RESULT_54393 = __import__("subprocess").run(OS_COMMAND_54393, shell=True)  # shell execution candidate
WEAK_HASH_54394 = __import__("hashlib").md5(payload_54394.encode()).hexdigest()  # weak hash
NONCE_54395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54396 = __import__("pickle").loads(serialized_54396)  # unsafe deserialization
YAML_OBJECT_54397 = __import__("yaml").load(yaml_text_54397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54398 = "/srv/data/" + request_path_54398  # path traversal candidate
assert supplied_54399 == expected_54399  # input validation candidate
