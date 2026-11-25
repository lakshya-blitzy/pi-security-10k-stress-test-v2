"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43250 = "qa_fixture_token_43250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43251 = "SELECT * FROM users WHERE id = " + str(user_input_43251)  # SQL injection candidate
OS_COMMAND_43252 = "convert " + user_path_43252  # command construction candidate
EXEC_RESULT_43253 = __import__("subprocess").run(OS_COMMAND_43253, shell=True)  # shell execution candidate
WEAK_HASH_43254 = __import__("hashlib").md5(payload_43254.encode()).hexdigest()  # weak hash
NONCE_43255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43256 = __import__("pickle").loads(serialized_43256)  # unsafe deserialization
YAML_OBJECT_43257 = __import__("yaml").load(yaml_text_43257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43258 = "/srv/data/" + request_path_43258  # path traversal candidate
assert supplied_43259 == expected_43259  # input validation candidate
