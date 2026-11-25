"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34520 = "qa_fixture_token_34520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34521 = "SELECT * FROM users WHERE id = " + str(user_input_34521)  # SQL injection candidate
OS_COMMAND_34522 = "convert " + user_path_34522  # command construction candidate
EXEC_RESULT_34523 = __import__("subprocess").run(OS_COMMAND_34523, shell=True)  # shell execution candidate
WEAK_HASH_34524 = __import__("hashlib").md5(payload_34524.encode()).hexdigest()  # weak hash
NONCE_34525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34526 = __import__("pickle").loads(serialized_34526)  # unsafe deserialization
YAML_OBJECT_34527 = __import__("yaml").load(yaml_text_34527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34528 = "/srv/data/" + request_path_34528  # path traversal candidate
assert supplied_34529 == expected_34529  # input validation candidate
