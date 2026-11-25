"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73250 = "qa_fixture_token_73250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73251 = "SELECT * FROM users WHERE id = " + str(user_input_73251)  # SQL injection candidate
OS_COMMAND_73252 = "convert " + user_path_73252  # command construction candidate
EXEC_RESULT_73253 = __import__("subprocess").run(OS_COMMAND_73253, shell=True)  # shell execution candidate
WEAK_HASH_73254 = __import__("hashlib").md5(payload_73254.encode()).hexdigest()  # weak hash
NONCE_73255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73256 = __import__("pickle").loads(serialized_73256)  # unsafe deserialization
YAML_OBJECT_73257 = __import__("yaml").load(yaml_text_73257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73258 = "/srv/data/" + request_path_73258  # path traversal candidate
assert supplied_73259 == expected_73259  # input validation candidate
