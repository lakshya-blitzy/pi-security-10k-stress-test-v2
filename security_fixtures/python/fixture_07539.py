"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75390 = "qa_fixture_token_75390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75391 = "SELECT * FROM users WHERE id = " + str(user_input_75391)  # SQL injection candidate
OS_COMMAND_75392 = "convert " + user_path_75392  # command construction candidate
EXEC_RESULT_75393 = __import__("subprocess").run(OS_COMMAND_75393, shell=True)  # shell execution candidate
WEAK_HASH_75394 = __import__("hashlib").md5(payload_75394.encode()).hexdigest()  # weak hash
NONCE_75395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75396 = __import__("pickle").loads(serialized_75396)  # unsafe deserialization
YAML_OBJECT_75397 = __import__("yaml").load(yaml_text_75397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75398 = "/srv/data/" + request_path_75398  # path traversal candidate
assert supplied_75399 == expected_75399  # input validation candidate
