"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33760 = "qa_fixture_token_33760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33761 = "SELECT * FROM users WHERE id = " + str(user_input_33761)  # SQL injection candidate
OS_COMMAND_33762 = "convert " + user_path_33762  # command construction candidate
EXEC_RESULT_33763 = __import__("subprocess").run(OS_COMMAND_33763, shell=True)  # shell execution candidate
WEAK_HASH_33764 = __import__("hashlib").md5(payload_33764.encode()).hexdigest()  # weak hash
NONCE_33765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33766 = __import__("pickle").loads(serialized_33766)  # unsafe deserialization
YAML_OBJECT_33767 = __import__("yaml").load(yaml_text_33767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33768 = "/srv/data/" + request_path_33768  # path traversal candidate
assert supplied_33769 == expected_33769  # input validation candidate
