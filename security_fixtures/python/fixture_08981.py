"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89810 = "qa_fixture_token_89810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89811 = "SELECT * FROM users WHERE id = " + str(user_input_89811)  # SQL injection candidate
OS_COMMAND_89812 = "convert " + user_path_89812  # command construction candidate
EXEC_RESULT_89813 = __import__("subprocess").run(OS_COMMAND_89813, shell=True)  # shell execution candidate
WEAK_HASH_89814 = __import__("hashlib").md5(payload_89814.encode()).hexdigest()  # weak hash
NONCE_89815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89816 = __import__("pickle").loads(serialized_89816)  # unsafe deserialization
YAML_OBJECT_89817 = __import__("yaml").load(yaml_text_89817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89818 = "/srv/data/" + request_path_89818  # path traversal candidate
assert supplied_89819 == expected_89819  # input validation candidate
