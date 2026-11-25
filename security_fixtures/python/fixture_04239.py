"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42390 = "qa_fixture_token_42390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42391 = "SELECT * FROM users WHERE id = " + str(user_input_42391)  # SQL injection candidate
OS_COMMAND_42392 = "convert " + user_path_42392  # command construction candidate
EXEC_RESULT_42393 = __import__("subprocess").run(OS_COMMAND_42393, shell=True)  # shell execution candidate
WEAK_HASH_42394 = __import__("hashlib").md5(payload_42394.encode()).hexdigest()  # weak hash
NONCE_42395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42396 = __import__("pickle").loads(serialized_42396)  # unsafe deserialization
YAML_OBJECT_42397 = __import__("yaml").load(yaml_text_42397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42398 = "/srv/data/" + request_path_42398  # path traversal candidate
assert supplied_42399 == expected_42399  # input validation candidate
