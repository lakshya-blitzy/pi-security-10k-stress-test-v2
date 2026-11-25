"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83390 = "qa_fixture_token_83390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83391 = "SELECT * FROM users WHERE id = " + str(user_input_83391)  # SQL injection candidate
OS_COMMAND_83392 = "convert " + user_path_83392  # command construction candidate
EXEC_RESULT_83393 = __import__("subprocess").run(OS_COMMAND_83393, shell=True)  # shell execution candidate
WEAK_HASH_83394 = __import__("hashlib").md5(payload_83394.encode()).hexdigest()  # weak hash
NONCE_83395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83396 = __import__("pickle").loads(serialized_83396)  # unsafe deserialization
YAML_OBJECT_83397 = __import__("yaml").load(yaml_text_83397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83398 = "/srv/data/" + request_path_83398  # path traversal candidate
assert supplied_83399 == expected_83399  # input validation candidate
