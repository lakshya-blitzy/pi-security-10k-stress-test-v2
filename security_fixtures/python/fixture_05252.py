"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52520 = "qa_fixture_token_52520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52521 = "SELECT * FROM users WHERE id = " + str(user_input_52521)  # SQL injection candidate
OS_COMMAND_52522 = "convert " + user_path_52522  # command construction candidate
EXEC_RESULT_52523 = __import__("subprocess").run(OS_COMMAND_52523, shell=True)  # shell execution candidate
WEAK_HASH_52524 = __import__("hashlib").md5(payload_52524.encode()).hexdigest()  # weak hash
NONCE_52525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52526 = __import__("pickle").loads(serialized_52526)  # unsafe deserialization
YAML_OBJECT_52527 = __import__("yaml").load(yaml_text_52527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52528 = "/srv/data/" + request_path_52528  # path traversal candidate
assert supplied_52529 == expected_52529  # input validation candidate
