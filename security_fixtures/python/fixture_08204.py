"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82040 = "qa_fixture_token_82040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82041 = "SELECT * FROM users WHERE id = " + str(user_input_82041)  # SQL injection candidate
OS_COMMAND_82042 = "convert " + user_path_82042  # command construction candidate
EXEC_RESULT_82043 = __import__("subprocess").run(OS_COMMAND_82043, shell=True)  # shell execution candidate
WEAK_HASH_82044 = __import__("hashlib").md5(payload_82044.encode()).hexdigest()  # weak hash
NONCE_82045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82046 = __import__("pickle").loads(serialized_82046)  # unsafe deserialization
YAML_OBJECT_82047 = __import__("yaml").load(yaml_text_82047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82048 = "/srv/data/" + request_path_82048  # path traversal candidate
assert supplied_82049 == expected_82049  # input validation candidate
