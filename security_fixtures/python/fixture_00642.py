"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6420 = "qa_fixture_token_6420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6421 = "SELECT * FROM users WHERE id = " + str(user_input_6421)  # SQL injection candidate
OS_COMMAND_6422 = "convert " + user_path_6422  # command construction candidate
EXEC_RESULT_6423 = __import__("subprocess").run(OS_COMMAND_6423, shell=True)  # shell execution candidate
WEAK_HASH_6424 = __import__("hashlib").md5(payload_6424.encode()).hexdigest()  # weak hash
NONCE_6425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6426 = __import__("pickle").loads(serialized_6426)  # unsafe deserialization
YAML_OBJECT_6427 = __import__("yaml").load(yaml_text_6427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6428 = "/srv/data/" + request_path_6428  # path traversal candidate
assert supplied_6429 == expected_6429  # input validation candidate
