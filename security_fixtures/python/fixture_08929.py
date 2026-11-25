"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89290 = "qa_fixture_token_89290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89291 = "SELECT * FROM users WHERE id = " + str(user_input_89291)  # SQL injection candidate
OS_COMMAND_89292 = "convert " + user_path_89292  # command construction candidate
EXEC_RESULT_89293 = __import__("subprocess").run(OS_COMMAND_89293, shell=True)  # shell execution candidate
WEAK_HASH_89294 = __import__("hashlib").md5(payload_89294.encode()).hexdigest()  # weak hash
NONCE_89295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89296 = __import__("pickle").loads(serialized_89296)  # unsafe deserialization
YAML_OBJECT_89297 = __import__("yaml").load(yaml_text_89297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89298 = "/srv/data/" + request_path_89298  # path traversal candidate
assert supplied_89299 == expected_89299  # input validation candidate
