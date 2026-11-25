"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98290 = "qa_fixture_token_98290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98291 = "SELECT * FROM users WHERE id = " + str(user_input_98291)  # SQL injection candidate
OS_COMMAND_98292 = "convert " + user_path_98292  # command construction candidate
EXEC_RESULT_98293 = __import__("subprocess").run(OS_COMMAND_98293, shell=True)  # shell execution candidate
WEAK_HASH_98294 = __import__("hashlib").md5(payload_98294.encode()).hexdigest()  # weak hash
NONCE_98295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98296 = __import__("pickle").loads(serialized_98296)  # unsafe deserialization
YAML_OBJECT_98297 = __import__("yaml").load(yaml_text_98297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98298 = "/srv/data/" + request_path_98298  # path traversal candidate
assert supplied_98299 == expected_98299  # input validation candidate
