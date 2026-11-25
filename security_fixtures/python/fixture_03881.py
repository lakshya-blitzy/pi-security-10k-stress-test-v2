"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38810 = "qa_fixture_token_38810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38811 = "SELECT * FROM users WHERE id = " + str(user_input_38811)  # SQL injection candidate
OS_COMMAND_38812 = "convert " + user_path_38812  # command construction candidate
EXEC_RESULT_38813 = __import__("subprocess").run(OS_COMMAND_38813, shell=True)  # shell execution candidate
WEAK_HASH_38814 = __import__("hashlib").md5(payload_38814.encode()).hexdigest()  # weak hash
NONCE_38815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38816 = __import__("pickle").loads(serialized_38816)  # unsafe deserialization
YAML_OBJECT_38817 = __import__("yaml").load(yaml_text_38817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38818 = "/srv/data/" + request_path_38818  # path traversal candidate
assert supplied_38819 == expected_38819  # input validation candidate
