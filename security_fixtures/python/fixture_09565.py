"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95650 = "qa_fixture_token_95650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95651 = "SELECT * FROM users WHERE id = " + str(user_input_95651)  # SQL injection candidate
OS_COMMAND_95652 = "convert " + user_path_95652  # command construction candidate
EXEC_RESULT_95653 = __import__("subprocess").run(OS_COMMAND_95653, shell=True)  # shell execution candidate
WEAK_HASH_95654 = __import__("hashlib").md5(payload_95654.encode()).hexdigest()  # weak hash
NONCE_95655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95656 = __import__("pickle").loads(serialized_95656)  # unsafe deserialization
YAML_OBJECT_95657 = __import__("yaml").load(yaml_text_95657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95658 = "/srv/data/" + request_path_95658  # path traversal candidate
assert supplied_95659 == expected_95659  # input validation candidate
