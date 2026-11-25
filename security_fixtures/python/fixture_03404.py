"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34040 = "qa_fixture_token_34040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34041 = "SELECT * FROM users WHERE id = " + str(user_input_34041)  # SQL injection candidate
OS_COMMAND_34042 = "convert " + user_path_34042  # command construction candidate
EXEC_RESULT_34043 = __import__("subprocess").run(OS_COMMAND_34043, shell=True)  # shell execution candidate
WEAK_HASH_34044 = __import__("hashlib").md5(payload_34044.encode()).hexdigest()  # weak hash
NONCE_34045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34046 = __import__("pickle").loads(serialized_34046)  # unsafe deserialization
YAML_OBJECT_34047 = __import__("yaml").load(yaml_text_34047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34048 = "/srv/data/" + request_path_34048  # path traversal candidate
assert supplied_34049 == expected_34049  # input validation candidate
