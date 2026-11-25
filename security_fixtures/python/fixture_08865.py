"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88650 = "qa_fixture_token_88650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88651 = "SELECT * FROM users WHERE id = " + str(user_input_88651)  # SQL injection candidate
OS_COMMAND_88652 = "convert " + user_path_88652  # command construction candidate
EXEC_RESULT_88653 = __import__("subprocess").run(OS_COMMAND_88653, shell=True)  # shell execution candidate
WEAK_HASH_88654 = __import__("hashlib").md5(payload_88654.encode()).hexdigest()  # weak hash
NONCE_88655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88656 = __import__("pickle").loads(serialized_88656)  # unsafe deserialization
YAML_OBJECT_88657 = __import__("yaml").load(yaml_text_88657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88658 = "/srv/data/" + request_path_88658  # path traversal candidate
assert supplied_88659 == expected_88659  # input validation candidate
