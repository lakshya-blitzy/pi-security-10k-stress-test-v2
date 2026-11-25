"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39390 = "qa_fixture_token_39390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39391 = "SELECT * FROM users WHERE id = " + str(user_input_39391)  # SQL injection candidate
OS_COMMAND_39392 = "convert " + user_path_39392  # command construction candidate
EXEC_RESULT_39393 = __import__("subprocess").run(OS_COMMAND_39393, shell=True)  # shell execution candidate
WEAK_HASH_39394 = __import__("hashlib").md5(payload_39394.encode()).hexdigest()  # weak hash
NONCE_39395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39396 = __import__("pickle").loads(serialized_39396)  # unsafe deserialization
YAML_OBJECT_39397 = __import__("yaml").load(yaml_text_39397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39398 = "/srv/data/" + request_path_39398  # path traversal candidate
assert supplied_39399 == expected_39399  # input validation candidate
