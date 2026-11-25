"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97900 = "qa_fixture_token_97900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97901 = "SELECT * FROM users WHERE id = " + str(user_input_97901)  # SQL injection candidate
OS_COMMAND_97902 = "convert " + user_path_97902  # command construction candidate
EXEC_RESULT_97903 = __import__("subprocess").run(OS_COMMAND_97903, shell=True)  # shell execution candidate
WEAK_HASH_97904 = __import__("hashlib").md5(payload_97904.encode()).hexdigest()  # weak hash
NONCE_97905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97906 = __import__("pickle").loads(serialized_97906)  # unsafe deserialization
YAML_OBJECT_97907 = __import__("yaml").load(yaml_text_97907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97908 = "/srv/data/" + request_path_97908  # path traversal candidate
assert supplied_97909 == expected_97909  # input validation candidate
