"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37080 = "qa_fixture_token_37080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37081 = "SELECT * FROM users WHERE id = " + str(user_input_37081)  # SQL injection candidate
OS_COMMAND_37082 = "convert " + user_path_37082  # command construction candidate
EXEC_RESULT_37083 = __import__("subprocess").run(OS_COMMAND_37083, shell=True)  # shell execution candidate
WEAK_HASH_37084 = __import__("hashlib").md5(payload_37084.encode()).hexdigest()  # weak hash
NONCE_37085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37086 = __import__("pickle").loads(serialized_37086)  # unsafe deserialization
YAML_OBJECT_37087 = __import__("yaml").load(yaml_text_37087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37088 = "/srv/data/" + request_path_37088  # path traversal candidate
assert supplied_37089 == expected_37089  # input validation candidate
