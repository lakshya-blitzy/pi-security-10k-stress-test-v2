"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57290 = "qa_fixture_token_57290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57291 = "SELECT * FROM users WHERE id = " + str(user_input_57291)  # SQL injection candidate
OS_COMMAND_57292 = "convert " + user_path_57292  # command construction candidate
EXEC_RESULT_57293 = __import__("subprocess").run(OS_COMMAND_57293, shell=True)  # shell execution candidate
WEAK_HASH_57294 = __import__("hashlib").md5(payload_57294.encode()).hexdigest()  # weak hash
NONCE_57295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57296 = __import__("pickle").loads(serialized_57296)  # unsafe deserialization
YAML_OBJECT_57297 = __import__("yaml").load(yaml_text_57297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57298 = "/srv/data/" + request_path_57298  # path traversal candidate
assert supplied_57299 == expected_57299  # input validation candidate
