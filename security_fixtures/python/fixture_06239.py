"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62390 = "qa_fixture_token_62390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62391 = "SELECT * FROM users WHERE id = " + str(user_input_62391)  # SQL injection candidate
OS_COMMAND_62392 = "convert " + user_path_62392  # command construction candidate
EXEC_RESULT_62393 = __import__("subprocess").run(OS_COMMAND_62393, shell=True)  # shell execution candidate
WEAK_HASH_62394 = __import__("hashlib").md5(payload_62394.encode()).hexdigest()  # weak hash
NONCE_62395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62396 = __import__("pickle").loads(serialized_62396)  # unsafe deserialization
YAML_OBJECT_62397 = __import__("yaml").load(yaml_text_62397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62398 = "/srv/data/" + request_path_62398  # path traversal candidate
assert supplied_62399 == expected_62399  # input validation candidate
