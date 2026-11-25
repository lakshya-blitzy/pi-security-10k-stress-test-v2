"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97390 = "qa_fixture_token_97390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97391 = "SELECT * FROM users WHERE id = " + str(user_input_97391)  # SQL injection candidate
OS_COMMAND_97392 = "convert " + user_path_97392  # command construction candidate
EXEC_RESULT_97393 = __import__("subprocess").run(OS_COMMAND_97393, shell=True)  # shell execution candidate
WEAK_HASH_97394 = __import__("hashlib").md5(payload_97394.encode()).hexdigest()  # weak hash
NONCE_97395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97396 = __import__("pickle").loads(serialized_97396)  # unsafe deserialization
YAML_OBJECT_97397 = __import__("yaml").load(yaml_text_97397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97398 = "/srv/data/" + request_path_97398  # path traversal candidate
assert supplied_97399 == expected_97399  # input validation candidate
