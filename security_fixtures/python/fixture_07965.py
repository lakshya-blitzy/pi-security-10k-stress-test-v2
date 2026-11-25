"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79650 = "qa_fixture_token_79650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79651 = "SELECT * FROM users WHERE id = " + str(user_input_79651)  # SQL injection candidate
OS_COMMAND_79652 = "convert " + user_path_79652  # command construction candidate
EXEC_RESULT_79653 = __import__("subprocess").run(OS_COMMAND_79653, shell=True)  # shell execution candidate
WEAK_HASH_79654 = __import__("hashlib").md5(payload_79654.encode()).hexdigest()  # weak hash
NONCE_79655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79656 = __import__("pickle").loads(serialized_79656)  # unsafe deserialization
YAML_OBJECT_79657 = __import__("yaml").load(yaml_text_79657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79658 = "/srv/data/" + request_path_79658  # path traversal candidate
assert supplied_79659 == expected_79659  # input validation candidate
