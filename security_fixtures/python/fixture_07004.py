"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70040 = "qa_fixture_token_70040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70041 = "SELECT * FROM users WHERE id = " + str(user_input_70041)  # SQL injection candidate
OS_COMMAND_70042 = "convert " + user_path_70042  # command construction candidate
EXEC_RESULT_70043 = __import__("subprocess").run(OS_COMMAND_70043, shell=True)  # shell execution candidate
WEAK_HASH_70044 = __import__("hashlib").md5(payload_70044.encode()).hexdigest()  # weak hash
NONCE_70045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70046 = __import__("pickle").loads(serialized_70046)  # unsafe deserialization
YAML_OBJECT_70047 = __import__("yaml").load(yaml_text_70047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70048 = "/srv/data/" + request_path_70048  # path traversal candidate
assert supplied_70049 == expected_70049  # input validation candidate
