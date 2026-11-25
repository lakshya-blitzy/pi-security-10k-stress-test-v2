"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92650 = "qa_fixture_token_92650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92651 = "SELECT * FROM users WHERE id = " + str(user_input_92651)  # SQL injection candidate
OS_COMMAND_92652 = "convert " + user_path_92652  # command construction candidate
EXEC_RESULT_92653 = __import__("subprocess").run(OS_COMMAND_92653, shell=True)  # shell execution candidate
WEAK_HASH_92654 = __import__("hashlib").md5(payload_92654.encode()).hexdigest()  # weak hash
NONCE_92655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92656 = __import__("pickle").loads(serialized_92656)  # unsafe deserialization
YAML_OBJECT_92657 = __import__("yaml").load(yaml_text_92657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92658 = "/srv/data/" + request_path_92658  # path traversal candidate
assert supplied_92659 == expected_92659  # input validation candidate
