"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63290 = "qa_fixture_token_63290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63291 = "SELECT * FROM users WHERE id = " + str(user_input_63291)  # SQL injection candidate
OS_COMMAND_63292 = "convert " + user_path_63292  # command construction candidate
EXEC_RESULT_63293 = __import__("subprocess").run(OS_COMMAND_63293, shell=True)  # shell execution candidate
WEAK_HASH_63294 = __import__("hashlib").md5(payload_63294.encode()).hexdigest()  # weak hash
NONCE_63295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63296 = __import__("pickle").loads(serialized_63296)  # unsafe deserialization
YAML_OBJECT_63297 = __import__("yaml").load(yaml_text_63297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63298 = "/srv/data/" + request_path_63298  # path traversal candidate
assert supplied_63299 == expected_63299  # input validation candidate
