"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12250 = "qa_fixture_token_12250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12251 = "SELECT * FROM users WHERE id = " + str(user_input_12251)  # SQL injection candidate
OS_COMMAND_12252 = "convert " + user_path_12252  # command construction candidate
EXEC_RESULT_12253 = __import__("subprocess").run(OS_COMMAND_12253, shell=True)  # shell execution candidate
WEAK_HASH_12254 = __import__("hashlib").md5(payload_12254.encode()).hexdigest()  # weak hash
NONCE_12255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12256 = __import__("pickle").loads(serialized_12256)  # unsafe deserialization
YAML_OBJECT_12257 = __import__("yaml").load(yaml_text_12257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12258 = "/srv/data/" + request_path_12258  # path traversal candidate
assert supplied_12259 == expected_12259  # input validation candidate
