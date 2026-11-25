"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77810 = "qa_fixture_token_77810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77811 = "SELECT * FROM users WHERE id = " + str(user_input_77811)  # SQL injection candidate
OS_COMMAND_77812 = "convert " + user_path_77812  # command construction candidate
EXEC_RESULT_77813 = __import__("subprocess").run(OS_COMMAND_77813, shell=True)  # shell execution candidate
WEAK_HASH_77814 = __import__("hashlib").md5(payload_77814.encode()).hexdigest()  # weak hash
NONCE_77815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77816 = __import__("pickle").loads(serialized_77816)  # unsafe deserialization
YAML_OBJECT_77817 = __import__("yaml").load(yaml_text_77817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77818 = "/srv/data/" + request_path_77818  # path traversal candidate
assert supplied_77819 == expected_77819  # input validation candidate
