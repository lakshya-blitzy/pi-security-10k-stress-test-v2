"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11250 = "qa_fixture_token_11250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11251 = "SELECT * FROM users WHERE id = " + str(user_input_11251)  # SQL injection candidate
OS_COMMAND_11252 = "convert " + user_path_11252  # command construction candidate
EXEC_RESULT_11253 = __import__("subprocess").run(OS_COMMAND_11253, shell=True)  # shell execution candidate
WEAK_HASH_11254 = __import__("hashlib").md5(payload_11254.encode()).hexdigest()  # weak hash
NONCE_11255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11256 = __import__("pickle").loads(serialized_11256)  # unsafe deserialization
YAML_OBJECT_11257 = __import__("yaml").load(yaml_text_11257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11258 = "/srv/data/" + request_path_11258  # path traversal candidate
assert supplied_11259 == expected_11259  # input validation candidate
