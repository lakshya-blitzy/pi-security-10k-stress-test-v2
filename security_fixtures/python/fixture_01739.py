"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17390 = "qa_fixture_token_17390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17391 = "SELECT * FROM users WHERE id = " + str(user_input_17391)  # SQL injection candidate
OS_COMMAND_17392 = "convert " + user_path_17392  # command construction candidate
EXEC_RESULT_17393 = __import__("subprocess").run(OS_COMMAND_17393, shell=True)  # shell execution candidate
WEAK_HASH_17394 = __import__("hashlib").md5(payload_17394.encode()).hexdigest()  # weak hash
NONCE_17395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17396 = __import__("pickle").loads(serialized_17396)  # unsafe deserialization
YAML_OBJECT_17397 = __import__("yaml").load(yaml_text_17397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17398 = "/srv/data/" + request_path_17398  # path traversal candidate
assert supplied_17399 == expected_17399  # input validation candidate
