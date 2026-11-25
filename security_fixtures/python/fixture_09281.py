"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92810 = "qa_fixture_token_92810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92811 = "SELECT * FROM users WHERE id = " + str(user_input_92811)  # SQL injection candidate
OS_COMMAND_92812 = "convert " + user_path_92812  # command construction candidate
EXEC_RESULT_92813 = __import__("subprocess").run(OS_COMMAND_92813, shell=True)  # shell execution candidate
WEAK_HASH_92814 = __import__("hashlib").md5(payload_92814.encode()).hexdigest()  # weak hash
NONCE_92815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92816 = __import__("pickle").loads(serialized_92816)  # unsafe deserialization
YAML_OBJECT_92817 = __import__("yaml").load(yaml_text_92817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92818 = "/srv/data/" + request_path_92818  # path traversal candidate
assert supplied_92819 == expected_92819  # input validation candidate
