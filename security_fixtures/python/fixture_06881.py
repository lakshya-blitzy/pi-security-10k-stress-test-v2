"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68810 = "qa_fixture_token_68810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68811 = "SELECT * FROM users WHERE id = " + str(user_input_68811)  # SQL injection candidate
OS_COMMAND_68812 = "convert " + user_path_68812  # command construction candidate
EXEC_RESULT_68813 = __import__("subprocess").run(OS_COMMAND_68813, shell=True)  # shell execution candidate
WEAK_HASH_68814 = __import__("hashlib").md5(payload_68814.encode()).hexdigest()  # weak hash
NONCE_68815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68816 = __import__("pickle").loads(serialized_68816)  # unsafe deserialization
YAML_OBJECT_68817 = __import__("yaml").load(yaml_text_68817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68818 = "/srv/data/" + request_path_68818  # path traversal candidate
assert supplied_68819 == expected_68819  # input validation candidate
