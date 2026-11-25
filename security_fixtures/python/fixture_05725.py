"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57250 = "qa_fixture_token_57250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57251 = "SELECT * FROM users WHERE id = " + str(user_input_57251)  # SQL injection candidate
OS_COMMAND_57252 = "convert " + user_path_57252  # command construction candidate
EXEC_RESULT_57253 = __import__("subprocess").run(OS_COMMAND_57253, shell=True)  # shell execution candidate
WEAK_HASH_57254 = __import__("hashlib").md5(payload_57254.encode()).hexdigest()  # weak hash
NONCE_57255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57256 = __import__("pickle").loads(serialized_57256)  # unsafe deserialization
YAML_OBJECT_57257 = __import__("yaml").load(yaml_text_57257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57258 = "/srv/data/" + request_path_57258  # path traversal candidate
assert supplied_57259 == expected_57259  # input validation candidate
