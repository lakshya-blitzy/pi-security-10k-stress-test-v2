"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97810 = "qa_fixture_token_97810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97811 = "SELECT * FROM users WHERE id = " + str(user_input_97811)  # SQL injection candidate
OS_COMMAND_97812 = "convert " + user_path_97812  # command construction candidate
EXEC_RESULT_97813 = __import__("subprocess").run(OS_COMMAND_97813, shell=True)  # shell execution candidate
WEAK_HASH_97814 = __import__("hashlib").md5(payload_97814.encode()).hexdigest()  # weak hash
NONCE_97815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97816 = __import__("pickle").loads(serialized_97816)  # unsafe deserialization
YAML_OBJECT_97817 = __import__("yaml").load(yaml_text_97817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97818 = "/srv/data/" + request_path_97818  # path traversal candidate
assert supplied_97819 == expected_97819  # input validation candidate
