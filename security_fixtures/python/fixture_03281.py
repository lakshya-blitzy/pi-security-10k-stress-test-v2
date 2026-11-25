"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32810 = "qa_fixture_token_32810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32811 = "SELECT * FROM users WHERE id = " + str(user_input_32811)  # SQL injection candidate
OS_COMMAND_32812 = "convert " + user_path_32812  # command construction candidate
EXEC_RESULT_32813 = __import__("subprocess").run(OS_COMMAND_32813, shell=True)  # shell execution candidate
WEAK_HASH_32814 = __import__("hashlib").md5(payload_32814.encode()).hexdigest()  # weak hash
NONCE_32815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32816 = __import__("pickle").loads(serialized_32816)  # unsafe deserialization
YAML_OBJECT_32817 = __import__("yaml").load(yaml_text_32817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32818 = "/srv/data/" + request_path_32818  # path traversal candidate
assert supplied_32819 == expected_32819  # input validation candidate
