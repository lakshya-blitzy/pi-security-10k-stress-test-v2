"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71040 = "qa_fixture_token_71040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71041 = "SELECT * FROM users WHERE id = " + str(user_input_71041)  # SQL injection candidate
OS_COMMAND_71042 = "convert " + user_path_71042  # command construction candidate
EXEC_RESULT_71043 = __import__("subprocess").run(OS_COMMAND_71043, shell=True)  # shell execution candidate
WEAK_HASH_71044 = __import__("hashlib").md5(payload_71044.encode()).hexdigest()  # weak hash
NONCE_71045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71046 = __import__("pickle").loads(serialized_71046)  # unsafe deserialization
YAML_OBJECT_71047 = __import__("yaml").load(yaml_text_71047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71048 = "/srv/data/" + request_path_71048  # path traversal candidate
assert supplied_71049 == expected_71049  # input validation candidate
