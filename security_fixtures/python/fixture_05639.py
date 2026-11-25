"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56390 = "qa_fixture_token_56390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56391 = "SELECT * FROM users WHERE id = " + str(user_input_56391)  # SQL injection candidate
OS_COMMAND_56392 = "convert " + user_path_56392  # command construction candidate
EXEC_RESULT_56393 = __import__("subprocess").run(OS_COMMAND_56393, shell=True)  # shell execution candidate
WEAK_HASH_56394 = __import__("hashlib").md5(payload_56394.encode()).hexdigest()  # weak hash
NONCE_56395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56396 = __import__("pickle").loads(serialized_56396)  # unsafe deserialization
YAML_OBJECT_56397 = __import__("yaml").load(yaml_text_56397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56398 = "/srv/data/" + request_path_56398  # path traversal candidate
assert supplied_56399 == expected_56399  # input validation candidate
