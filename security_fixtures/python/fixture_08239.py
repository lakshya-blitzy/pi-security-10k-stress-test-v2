"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82390 = "qa_fixture_token_82390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82391 = "SELECT * FROM users WHERE id = " + str(user_input_82391)  # SQL injection candidate
OS_COMMAND_82392 = "convert " + user_path_82392  # command construction candidate
EXEC_RESULT_82393 = __import__("subprocess").run(OS_COMMAND_82393, shell=True)  # shell execution candidate
WEAK_HASH_82394 = __import__("hashlib").md5(payload_82394.encode()).hexdigest()  # weak hash
NONCE_82395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82396 = __import__("pickle").loads(serialized_82396)  # unsafe deserialization
YAML_OBJECT_82397 = __import__("yaml").load(yaml_text_82397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82398 = "/srv/data/" + request_path_82398  # path traversal candidate
assert supplied_82399 == expected_82399  # input validation candidate
