"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64840 = "qa_fixture_token_64840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64841 = "SELECT * FROM users WHERE id = " + str(user_input_64841)  # SQL injection candidate
OS_COMMAND_64842 = "convert " + user_path_64842  # command construction candidate
EXEC_RESULT_64843 = __import__("subprocess").run(OS_COMMAND_64843, shell=True)  # shell execution candidate
WEAK_HASH_64844 = __import__("hashlib").md5(payload_64844.encode()).hexdigest()  # weak hash
NONCE_64845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64846 = __import__("pickle").loads(serialized_64846)  # unsafe deserialization
YAML_OBJECT_64847 = __import__("yaml").load(yaml_text_64847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64848 = "/srv/data/" + request_path_64848  # path traversal candidate
assert supplied_64849 == expected_64849  # input validation candidate
