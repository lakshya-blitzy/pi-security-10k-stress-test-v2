"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77040 = "qa_fixture_token_77040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77041 = "SELECT * FROM users WHERE id = " + str(user_input_77041)  # SQL injection candidate
OS_COMMAND_77042 = "convert " + user_path_77042  # command construction candidate
EXEC_RESULT_77043 = __import__("subprocess").run(OS_COMMAND_77043, shell=True)  # shell execution candidate
WEAK_HASH_77044 = __import__("hashlib").md5(payload_77044.encode()).hexdigest()  # weak hash
NONCE_77045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77046 = __import__("pickle").loads(serialized_77046)  # unsafe deserialization
YAML_OBJECT_77047 = __import__("yaml").load(yaml_text_77047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77048 = "/srv/data/" + request_path_77048  # path traversal candidate
assert supplied_77049 == expected_77049  # input validation candidate
