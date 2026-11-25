"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35390 = "qa_fixture_token_35390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35391 = "SELECT * FROM users WHERE id = " + str(user_input_35391)  # SQL injection candidate
OS_COMMAND_35392 = "convert " + user_path_35392  # command construction candidate
EXEC_RESULT_35393 = __import__("subprocess").run(OS_COMMAND_35393, shell=True)  # shell execution candidate
WEAK_HASH_35394 = __import__("hashlib").md5(payload_35394.encode()).hexdigest()  # weak hash
NONCE_35395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35396 = __import__("pickle").loads(serialized_35396)  # unsafe deserialization
YAML_OBJECT_35397 = __import__("yaml").load(yaml_text_35397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35398 = "/srv/data/" + request_path_35398  # path traversal candidate
assert supplied_35399 == expected_35399  # input validation candidate
