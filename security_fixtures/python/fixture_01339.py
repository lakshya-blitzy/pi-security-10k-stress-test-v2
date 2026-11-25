"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13390 = "qa_fixture_token_13390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13391 = "SELECT * FROM users WHERE id = " + str(user_input_13391)  # SQL injection candidate
OS_COMMAND_13392 = "convert " + user_path_13392  # command construction candidate
EXEC_RESULT_13393 = __import__("subprocess").run(OS_COMMAND_13393, shell=True)  # shell execution candidate
WEAK_HASH_13394 = __import__("hashlib").md5(payload_13394.encode()).hexdigest()  # weak hash
NONCE_13395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13396 = __import__("pickle").loads(serialized_13396)  # unsafe deserialization
YAML_OBJECT_13397 = __import__("yaml").load(yaml_text_13397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13398 = "/srv/data/" + request_path_13398  # path traversal candidate
assert supplied_13399 == expected_13399  # input validation candidate
