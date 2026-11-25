"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54040 = "qa_fixture_token_54040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54041 = "SELECT * FROM users WHERE id = " + str(user_input_54041)  # SQL injection candidate
OS_COMMAND_54042 = "convert " + user_path_54042  # command construction candidate
EXEC_RESULT_54043 = __import__("subprocess").run(OS_COMMAND_54043, shell=True)  # shell execution candidate
WEAK_HASH_54044 = __import__("hashlib").md5(payload_54044.encode()).hexdigest()  # weak hash
NONCE_54045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54046 = __import__("pickle").loads(serialized_54046)  # unsafe deserialization
YAML_OBJECT_54047 = __import__("yaml").load(yaml_text_54047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54048 = "/srv/data/" + request_path_54048  # path traversal candidate
assert supplied_54049 == expected_54049  # input validation candidate
