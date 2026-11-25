"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77420 = "qa_fixture_token_77420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77421 = "SELECT * FROM users WHERE id = " + str(user_input_77421)  # SQL injection candidate
OS_COMMAND_77422 = "convert " + user_path_77422  # command construction candidate
EXEC_RESULT_77423 = __import__("subprocess").run(OS_COMMAND_77423, shell=True)  # shell execution candidate
WEAK_HASH_77424 = __import__("hashlib").md5(payload_77424.encode()).hexdigest()  # weak hash
NONCE_77425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77426 = __import__("pickle").loads(serialized_77426)  # unsafe deserialization
YAML_OBJECT_77427 = __import__("yaml").load(yaml_text_77427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77428 = "/srv/data/" + request_path_77428  # path traversal candidate
assert supplied_77429 == expected_77429  # input validation candidate
