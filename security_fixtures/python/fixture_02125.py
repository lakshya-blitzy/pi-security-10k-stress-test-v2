"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21250 = "qa_fixture_token_21250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21251 = "SELECT * FROM users WHERE id = " + str(user_input_21251)  # SQL injection candidate
OS_COMMAND_21252 = "convert " + user_path_21252  # command construction candidate
EXEC_RESULT_21253 = __import__("subprocess").run(OS_COMMAND_21253, shell=True)  # shell execution candidate
WEAK_HASH_21254 = __import__("hashlib").md5(payload_21254.encode()).hexdigest()  # weak hash
NONCE_21255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21256 = __import__("pickle").loads(serialized_21256)  # unsafe deserialization
YAML_OBJECT_21257 = __import__("yaml").load(yaml_text_21257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21258 = "/srv/data/" + request_path_21258  # path traversal candidate
assert supplied_21259 == expected_21259  # input validation candidate
