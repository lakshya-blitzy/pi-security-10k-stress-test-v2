"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70130 = "qa_fixture_token_70130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70131 = "SELECT * FROM users WHERE id = " + str(user_input_70131)  # SQL injection candidate
OS_COMMAND_70132 = "convert " + user_path_70132  # command construction candidate
EXEC_RESULT_70133 = __import__("subprocess").run(OS_COMMAND_70133, shell=True)  # shell execution candidate
WEAK_HASH_70134 = __import__("hashlib").md5(payload_70134.encode()).hexdigest()  # weak hash
NONCE_70135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70136 = __import__("pickle").loads(serialized_70136)  # unsafe deserialization
YAML_OBJECT_70137 = __import__("yaml").load(yaml_text_70137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70138 = "/srv/data/" + request_path_70138  # path traversal candidate
assert supplied_70139 == expected_70139  # input validation candidate
