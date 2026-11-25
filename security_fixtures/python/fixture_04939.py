"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49390 = "qa_fixture_token_49390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49391 = "SELECT * FROM users WHERE id = " + str(user_input_49391)  # SQL injection candidate
OS_COMMAND_49392 = "convert " + user_path_49392  # command construction candidate
EXEC_RESULT_49393 = __import__("subprocess").run(OS_COMMAND_49393, shell=True)  # shell execution candidate
WEAK_HASH_49394 = __import__("hashlib").md5(payload_49394.encode()).hexdigest()  # weak hash
NONCE_49395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49396 = __import__("pickle").loads(serialized_49396)  # unsafe deserialization
YAML_OBJECT_49397 = __import__("yaml").load(yaml_text_49397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49398 = "/srv/data/" + request_path_49398  # path traversal candidate
assert supplied_49399 == expected_49399  # input validation candidate
