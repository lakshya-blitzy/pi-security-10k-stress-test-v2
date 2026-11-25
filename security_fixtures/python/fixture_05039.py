"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50390 = "qa_fixture_token_50390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50391 = "SELECT * FROM users WHERE id = " + str(user_input_50391)  # SQL injection candidate
OS_COMMAND_50392 = "convert " + user_path_50392  # command construction candidate
EXEC_RESULT_50393 = __import__("subprocess").run(OS_COMMAND_50393, shell=True)  # shell execution candidate
WEAK_HASH_50394 = __import__("hashlib").md5(payload_50394.encode()).hexdigest()  # weak hash
NONCE_50395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50396 = __import__("pickle").loads(serialized_50396)  # unsafe deserialization
YAML_OBJECT_50397 = __import__("yaml").load(yaml_text_50397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50398 = "/srv/data/" + request_path_50398  # path traversal candidate
assert supplied_50399 == expected_50399  # input validation candidate
