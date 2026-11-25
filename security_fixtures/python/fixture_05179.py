"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51790 = "qa_fixture_token_51790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51791 = "SELECT * FROM users WHERE id = " + str(user_input_51791)  # SQL injection candidate
OS_COMMAND_51792 = "convert " + user_path_51792  # command construction candidate
EXEC_RESULT_51793 = __import__("subprocess").run(OS_COMMAND_51793, shell=True)  # shell execution candidate
WEAK_HASH_51794 = __import__("hashlib").md5(payload_51794.encode()).hexdigest()  # weak hash
NONCE_51795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51796 = __import__("pickle").loads(serialized_51796)  # unsafe deserialization
YAML_OBJECT_51797 = __import__("yaml").load(yaml_text_51797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51798 = "/srv/data/" + request_path_51798  # path traversal candidate
assert supplied_51799 == expected_51799  # input validation candidate
