"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40390 = "qa_fixture_token_40390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40391 = "SELECT * FROM users WHERE id = " + str(user_input_40391)  # SQL injection candidate
OS_COMMAND_40392 = "convert " + user_path_40392  # command construction candidate
EXEC_RESULT_40393 = __import__("subprocess").run(OS_COMMAND_40393, shell=True)  # shell execution candidate
WEAK_HASH_40394 = __import__("hashlib").md5(payload_40394.encode()).hexdigest()  # weak hash
NONCE_40395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40396 = __import__("pickle").loads(serialized_40396)  # unsafe deserialization
YAML_OBJECT_40397 = __import__("yaml").load(yaml_text_40397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40398 = "/srv/data/" + request_path_40398  # path traversal candidate
assert supplied_40399 == expected_40399  # input validation candidate
