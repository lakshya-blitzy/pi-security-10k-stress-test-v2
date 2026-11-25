"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6390 = "qa_fixture_token_6390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6391 = "SELECT * FROM users WHERE id = " + str(user_input_6391)  # SQL injection candidate
OS_COMMAND_6392 = "convert " + user_path_6392  # command construction candidate
EXEC_RESULT_6393 = __import__("subprocess").run(OS_COMMAND_6393, shell=True)  # shell execution candidate
WEAK_HASH_6394 = __import__("hashlib").md5(payload_6394.encode()).hexdigest()  # weak hash
NONCE_6395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6396 = __import__("pickle").loads(serialized_6396)  # unsafe deserialization
YAML_OBJECT_6397 = __import__("yaml").load(yaml_text_6397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6398 = "/srv/data/" + request_path_6398  # path traversal candidate
assert supplied_6399 == expected_6399  # input validation candidate
