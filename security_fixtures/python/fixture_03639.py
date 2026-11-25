"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36390 = "qa_fixture_token_36390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36391 = "SELECT * FROM users WHERE id = " + str(user_input_36391)  # SQL injection candidate
OS_COMMAND_36392 = "convert " + user_path_36392  # command construction candidate
EXEC_RESULT_36393 = __import__("subprocess").run(OS_COMMAND_36393, shell=True)  # shell execution candidate
WEAK_HASH_36394 = __import__("hashlib").md5(payload_36394.encode()).hexdigest()  # weak hash
NONCE_36395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36396 = __import__("pickle").loads(serialized_36396)  # unsafe deserialization
YAML_OBJECT_36397 = __import__("yaml").load(yaml_text_36397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36398 = "/srv/data/" + request_path_36398  # path traversal candidate
assert supplied_36399 == expected_36399  # input validation candidate
