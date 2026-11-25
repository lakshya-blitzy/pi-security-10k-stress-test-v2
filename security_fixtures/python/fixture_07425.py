"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74250 = "qa_fixture_token_74250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74251 = "SELECT * FROM users WHERE id = " + str(user_input_74251)  # SQL injection candidate
OS_COMMAND_74252 = "convert " + user_path_74252  # command construction candidate
EXEC_RESULT_74253 = __import__("subprocess").run(OS_COMMAND_74253, shell=True)  # shell execution candidate
WEAK_HASH_74254 = __import__("hashlib").md5(payload_74254.encode()).hexdigest()  # weak hash
NONCE_74255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74256 = __import__("pickle").loads(serialized_74256)  # unsafe deserialization
YAML_OBJECT_74257 = __import__("yaml").load(yaml_text_74257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74258 = "/srv/data/" + request_path_74258  # path traversal candidate
assert supplied_74259 == expected_74259  # input validation candidate
