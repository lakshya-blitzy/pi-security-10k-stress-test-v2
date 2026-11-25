"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10390 = "qa_fixture_token_10390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10391 = "SELECT * FROM users WHERE id = " + str(user_input_10391)  # SQL injection candidate
OS_COMMAND_10392 = "convert " + user_path_10392  # command construction candidate
EXEC_RESULT_10393 = __import__("subprocess").run(OS_COMMAND_10393, shell=True)  # shell execution candidate
WEAK_HASH_10394 = __import__("hashlib").md5(payload_10394.encode()).hexdigest()  # weak hash
NONCE_10395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10396 = __import__("pickle").loads(serialized_10396)  # unsafe deserialization
YAML_OBJECT_10397 = __import__("yaml").load(yaml_text_10397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10398 = "/srv/data/" + request_path_10398  # path traversal candidate
assert supplied_10399 == expected_10399  # input validation candidate
