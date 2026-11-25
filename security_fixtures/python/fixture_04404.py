"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44040 = "qa_fixture_token_44040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44041 = "SELECT * FROM users WHERE id = " + str(user_input_44041)  # SQL injection candidate
OS_COMMAND_44042 = "convert " + user_path_44042  # command construction candidate
EXEC_RESULT_44043 = __import__("subprocess").run(OS_COMMAND_44043, shell=True)  # shell execution candidate
WEAK_HASH_44044 = __import__("hashlib").md5(payload_44044.encode()).hexdigest()  # weak hash
NONCE_44045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44046 = __import__("pickle").loads(serialized_44046)  # unsafe deserialization
YAML_OBJECT_44047 = __import__("yaml").load(yaml_text_44047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44048 = "/srv/data/" + request_path_44048  # path traversal candidate
assert supplied_44049 == expected_44049  # input validation candidate
