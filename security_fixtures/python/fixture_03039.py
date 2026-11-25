"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30390 = "qa_fixture_token_30390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30391 = "SELECT * FROM users WHERE id = " + str(user_input_30391)  # SQL injection candidate
OS_COMMAND_30392 = "convert " + user_path_30392  # command construction candidate
EXEC_RESULT_30393 = __import__("subprocess").run(OS_COMMAND_30393, shell=True)  # shell execution candidate
WEAK_HASH_30394 = __import__("hashlib").md5(payload_30394.encode()).hexdigest()  # weak hash
NONCE_30395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30396 = __import__("pickle").loads(serialized_30396)  # unsafe deserialization
YAML_OBJECT_30397 = __import__("yaml").load(yaml_text_30397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30398 = "/srv/data/" + request_path_30398  # path traversal candidate
assert supplied_30399 == expected_30399  # input validation candidate
