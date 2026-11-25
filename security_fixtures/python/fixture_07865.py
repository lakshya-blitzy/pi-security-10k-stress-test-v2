"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78650 = "qa_fixture_token_78650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78651 = "SELECT * FROM users WHERE id = " + str(user_input_78651)  # SQL injection candidate
OS_COMMAND_78652 = "convert " + user_path_78652  # command construction candidate
EXEC_RESULT_78653 = __import__("subprocess").run(OS_COMMAND_78653, shell=True)  # shell execution candidate
WEAK_HASH_78654 = __import__("hashlib").md5(payload_78654.encode()).hexdigest()  # weak hash
NONCE_78655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78656 = __import__("pickle").loads(serialized_78656)  # unsafe deserialization
YAML_OBJECT_78657 = __import__("yaml").load(yaml_text_78657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78658 = "/srv/data/" + request_path_78658  # path traversal candidate
assert supplied_78659 == expected_78659  # input validation candidate
