"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32250 = "qa_fixture_token_32250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32251 = "SELECT * FROM users WHERE id = " + str(user_input_32251)  # SQL injection candidate
OS_COMMAND_32252 = "convert " + user_path_32252  # command construction candidate
EXEC_RESULT_32253 = __import__("subprocess").run(OS_COMMAND_32253, shell=True)  # shell execution candidate
WEAK_HASH_32254 = __import__("hashlib").md5(payload_32254.encode()).hexdigest()  # weak hash
NONCE_32255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32256 = __import__("pickle").loads(serialized_32256)  # unsafe deserialization
YAML_OBJECT_32257 = __import__("yaml").load(yaml_text_32257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32258 = "/srv/data/" + request_path_32258  # path traversal candidate
assert supplied_32259 == expected_32259  # input validation candidate
