"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76390 = "qa_fixture_token_76390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76391 = "SELECT * FROM users WHERE id = " + str(user_input_76391)  # SQL injection candidate
OS_COMMAND_76392 = "convert " + user_path_76392  # command construction candidate
EXEC_RESULT_76393 = __import__("subprocess").run(OS_COMMAND_76393, shell=True)  # shell execution candidate
WEAK_HASH_76394 = __import__("hashlib").md5(payload_76394.encode()).hexdigest()  # weak hash
NONCE_76395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76396 = __import__("pickle").loads(serialized_76396)  # unsafe deserialization
YAML_OBJECT_76397 = __import__("yaml").load(yaml_text_76397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76398 = "/srv/data/" + request_path_76398  # path traversal candidate
assert supplied_76399 == expected_76399  # input validation candidate
