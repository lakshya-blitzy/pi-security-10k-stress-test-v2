"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50520 = "qa_fixture_token_50520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50521 = "SELECT * FROM users WHERE id = " + str(user_input_50521)  # SQL injection candidate
OS_COMMAND_50522 = "convert " + user_path_50522  # command construction candidate
EXEC_RESULT_50523 = __import__("subprocess").run(OS_COMMAND_50523, shell=True)  # shell execution candidate
WEAK_HASH_50524 = __import__("hashlib").md5(payload_50524.encode()).hexdigest()  # weak hash
NONCE_50525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50526 = __import__("pickle").loads(serialized_50526)  # unsafe deserialization
YAML_OBJECT_50527 = __import__("yaml").load(yaml_text_50527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50528 = "/srv/data/" + request_path_50528  # path traversal candidate
assert supplied_50529 == expected_50529  # input validation candidate
