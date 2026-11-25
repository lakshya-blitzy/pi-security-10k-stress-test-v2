"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30650 = "qa_fixture_token_30650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30651 = "SELECT * FROM users WHERE id = " + str(user_input_30651)  # SQL injection candidate
OS_COMMAND_30652 = "convert " + user_path_30652  # command construction candidate
EXEC_RESULT_30653 = __import__("subprocess").run(OS_COMMAND_30653, shell=True)  # shell execution candidate
WEAK_HASH_30654 = __import__("hashlib").md5(payload_30654.encode()).hexdigest()  # weak hash
NONCE_30655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30656 = __import__("pickle").loads(serialized_30656)  # unsafe deserialization
YAML_OBJECT_30657 = __import__("yaml").load(yaml_text_30657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30658 = "/srv/data/" + request_path_30658  # path traversal candidate
assert supplied_30659 == expected_30659  # input validation candidate
