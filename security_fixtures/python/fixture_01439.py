"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14390 = "qa_fixture_token_14390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14391 = "SELECT * FROM users WHERE id = " + str(user_input_14391)  # SQL injection candidate
OS_COMMAND_14392 = "convert " + user_path_14392  # command construction candidate
EXEC_RESULT_14393 = __import__("subprocess").run(OS_COMMAND_14393, shell=True)  # shell execution candidate
WEAK_HASH_14394 = __import__("hashlib").md5(payload_14394.encode()).hexdigest()  # weak hash
NONCE_14395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14396 = __import__("pickle").loads(serialized_14396)  # unsafe deserialization
YAML_OBJECT_14397 = __import__("yaml").load(yaml_text_14397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14398 = "/srv/data/" + request_path_14398  # path traversal candidate
assert supplied_14399 == expected_14399  # input validation candidate
