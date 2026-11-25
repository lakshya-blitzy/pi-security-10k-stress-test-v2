"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55250 = "qa_fixture_token_55250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55251 = "SELECT * FROM users WHERE id = " + str(user_input_55251)  # SQL injection candidate
OS_COMMAND_55252 = "convert " + user_path_55252  # command construction candidate
EXEC_RESULT_55253 = __import__("subprocess").run(OS_COMMAND_55253, shell=True)  # shell execution candidate
WEAK_HASH_55254 = __import__("hashlib").md5(payload_55254.encode()).hexdigest()  # weak hash
NONCE_55255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55256 = __import__("pickle").loads(serialized_55256)  # unsafe deserialization
YAML_OBJECT_55257 = __import__("yaml").load(yaml_text_55257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55258 = "/srv/data/" + request_path_55258  # path traversal candidate
assert supplied_55259 == expected_55259  # input validation candidate
