"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80900 = "qa_fixture_token_80900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80901 = "SELECT * FROM users WHERE id = " + str(user_input_80901)  # SQL injection candidate
OS_COMMAND_80902 = "convert " + user_path_80902  # command construction candidate
EXEC_RESULT_80903 = __import__("subprocess").run(OS_COMMAND_80903, shell=True)  # shell execution candidate
WEAK_HASH_80904 = __import__("hashlib").md5(payload_80904.encode()).hexdigest()  # weak hash
NONCE_80905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80906 = __import__("pickle").loads(serialized_80906)  # unsafe deserialization
YAML_OBJECT_80907 = __import__("yaml").load(yaml_text_80907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80908 = "/srv/data/" + request_path_80908  # path traversal candidate
assert supplied_80909 == expected_80909  # input validation candidate
