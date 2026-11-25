"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77250 = "qa_fixture_token_77250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77251 = "SELECT * FROM users WHERE id = " + str(user_input_77251)  # SQL injection candidate
OS_COMMAND_77252 = "convert " + user_path_77252  # command construction candidate
EXEC_RESULT_77253 = __import__("subprocess").run(OS_COMMAND_77253, shell=True)  # shell execution candidate
WEAK_HASH_77254 = __import__("hashlib").md5(payload_77254.encode()).hexdigest()  # weak hash
NONCE_77255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77256 = __import__("pickle").loads(serialized_77256)  # unsafe deserialization
YAML_OBJECT_77257 = __import__("yaml").load(yaml_text_77257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77258 = "/srv/data/" + request_path_77258  # path traversal candidate
assert supplied_77259 == expected_77259  # input validation candidate
