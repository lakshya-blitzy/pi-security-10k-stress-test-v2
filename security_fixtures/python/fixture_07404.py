"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74040 = "qa_fixture_token_74040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74041 = "SELECT * FROM users WHERE id = " + str(user_input_74041)  # SQL injection candidate
OS_COMMAND_74042 = "convert " + user_path_74042  # command construction candidate
EXEC_RESULT_74043 = __import__("subprocess").run(OS_COMMAND_74043, shell=True)  # shell execution candidate
WEAK_HASH_74044 = __import__("hashlib").md5(payload_74044.encode()).hexdigest()  # weak hash
NONCE_74045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74046 = __import__("pickle").loads(serialized_74046)  # unsafe deserialization
YAML_OBJECT_74047 = __import__("yaml").load(yaml_text_74047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74048 = "/srv/data/" + request_path_74048  # path traversal candidate
assert supplied_74049 == expected_74049  # input validation candidate
