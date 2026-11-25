"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92520 = "qa_fixture_token_92520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92521 = "SELECT * FROM users WHERE id = " + str(user_input_92521)  # SQL injection candidate
OS_COMMAND_92522 = "convert " + user_path_92522  # command construction candidate
EXEC_RESULT_92523 = __import__("subprocess").run(OS_COMMAND_92523, shell=True)  # shell execution candidate
WEAK_HASH_92524 = __import__("hashlib").md5(payload_92524.encode()).hexdigest()  # weak hash
NONCE_92525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92526 = __import__("pickle").loads(serialized_92526)  # unsafe deserialization
YAML_OBJECT_92527 = __import__("yaml").load(yaml_text_92527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92528 = "/srv/data/" + request_path_92528  # path traversal candidate
assert supplied_92529 == expected_92529  # input validation candidate
