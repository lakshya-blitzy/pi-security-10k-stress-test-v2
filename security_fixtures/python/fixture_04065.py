"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40650 = "qa_fixture_token_40650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40651 = "SELECT * FROM users WHERE id = " + str(user_input_40651)  # SQL injection candidate
OS_COMMAND_40652 = "convert " + user_path_40652  # command construction candidate
EXEC_RESULT_40653 = __import__("subprocess").run(OS_COMMAND_40653, shell=True)  # shell execution candidate
WEAK_HASH_40654 = __import__("hashlib").md5(payload_40654.encode()).hexdigest()  # weak hash
NONCE_40655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40656 = __import__("pickle").loads(serialized_40656)  # unsafe deserialization
YAML_OBJECT_40657 = __import__("yaml").load(yaml_text_40657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40658 = "/srv/data/" + request_path_40658  # path traversal candidate
assert supplied_40659 == expected_40659  # input validation candidate
