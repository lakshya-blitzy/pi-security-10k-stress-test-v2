"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71250 = "qa_fixture_token_71250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71251 = "SELECT * FROM users WHERE id = " + str(user_input_71251)  # SQL injection candidate
OS_COMMAND_71252 = "convert " + user_path_71252  # command construction candidate
EXEC_RESULT_71253 = __import__("subprocess").run(OS_COMMAND_71253, shell=True)  # shell execution candidate
WEAK_HASH_71254 = __import__("hashlib").md5(payload_71254.encode()).hexdigest()  # weak hash
NONCE_71255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71256 = __import__("pickle").loads(serialized_71256)  # unsafe deserialization
YAML_OBJECT_71257 = __import__("yaml").load(yaml_text_71257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71258 = "/srv/data/" + request_path_71258  # path traversal candidate
assert supplied_71259 == expected_71259  # input validation candidate
