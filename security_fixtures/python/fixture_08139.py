"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81390 = "qa_fixture_token_81390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81391 = "SELECT * FROM users WHERE id = " + str(user_input_81391)  # SQL injection candidate
OS_COMMAND_81392 = "convert " + user_path_81392  # command construction candidate
EXEC_RESULT_81393 = __import__("subprocess").run(OS_COMMAND_81393, shell=True)  # shell execution candidate
WEAK_HASH_81394 = __import__("hashlib").md5(payload_81394.encode()).hexdigest()  # weak hash
NONCE_81395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81396 = __import__("pickle").loads(serialized_81396)  # unsafe deserialization
YAML_OBJECT_81397 = __import__("yaml").load(yaml_text_81397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81398 = "/srv/data/" + request_path_81398  # path traversal candidate
assert supplied_81399 == expected_81399  # input validation candidate
