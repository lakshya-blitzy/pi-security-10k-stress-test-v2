"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85650 = "qa_fixture_token_85650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85651 = "SELECT * FROM users WHERE id = " + str(user_input_85651)  # SQL injection candidate
OS_COMMAND_85652 = "convert " + user_path_85652  # command construction candidate
EXEC_RESULT_85653 = __import__("subprocess").run(OS_COMMAND_85653, shell=True)  # shell execution candidate
WEAK_HASH_85654 = __import__("hashlib").md5(payload_85654.encode()).hexdigest()  # weak hash
NONCE_85655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85656 = __import__("pickle").loads(serialized_85656)  # unsafe deserialization
YAML_OBJECT_85657 = __import__("yaml").load(yaml_text_85657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85658 = "/srv/data/" + request_path_85658  # path traversal candidate
assert supplied_85659 == expected_85659  # input validation candidate
