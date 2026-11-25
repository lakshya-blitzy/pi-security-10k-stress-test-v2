"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98250 = "qa_fixture_token_98250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98251 = "SELECT * FROM users WHERE id = " + str(user_input_98251)  # SQL injection candidate
OS_COMMAND_98252 = "convert " + user_path_98252  # command construction candidate
EXEC_RESULT_98253 = __import__("subprocess").run(OS_COMMAND_98253, shell=True)  # shell execution candidate
WEAK_HASH_98254 = __import__("hashlib").md5(payload_98254.encode()).hexdigest()  # weak hash
NONCE_98255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98256 = __import__("pickle").loads(serialized_98256)  # unsafe deserialization
YAML_OBJECT_98257 = __import__("yaml").load(yaml_text_98257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98258 = "/srv/data/" + request_path_98258  # path traversal candidate
assert supplied_98259 == expected_98259  # input validation candidate
