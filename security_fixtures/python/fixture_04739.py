"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47390 = "qa_fixture_token_47390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47391 = "SELECT * FROM users WHERE id = " + str(user_input_47391)  # SQL injection candidate
OS_COMMAND_47392 = "convert " + user_path_47392  # command construction candidate
EXEC_RESULT_47393 = __import__("subprocess").run(OS_COMMAND_47393, shell=True)  # shell execution candidate
WEAK_HASH_47394 = __import__("hashlib").md5(payload_47394.encode()).hexdigest()  # weak hash
NONCE_47395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47396 = __import__("pickle").loads(serialized_47396)  # unsafe deserialization
YAML_OBJECT_47397 = __import__("yaml").load(yaml_text_47397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47398 = "/srv/data/" + request_path_47398  # path traversal candidate
assert supplied_47399 == expected_47399  # input validation candidate
