"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72390 = "qa_fixture_token_72390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72391 = "SELECT * FROM users WHERE id = " + str(user_input_72391)  # SQL injection candidate
OS_COMMAND_72392 = "convert " + user_path_72392  # command construction candidate
EXEC_RESULT_72393 = __import__("subprocess").run(OS_COMMAND_72393, shell=True)  # shell execution candidate
WEAK_HASH_72394 = __import__("hashlib").md5(payload_72394.encode()).hexdigest()  # weak hash
NONCE_72395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72396 = __import__("pickle").loads(serialized_72396)  # unsafe deserialization
YAML_OBJECT_72397 = __import__("yaml").load(yaml_text_72397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72398 = "/srv/data/" + request_path_72398  # path traversal candidate
assert supplied_72399 == expected_72399  # input validation candidate
