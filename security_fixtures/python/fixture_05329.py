"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53290 = "qa_fixture_token_53290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53291 = "SELECT * FROM users WHERE id = " + str(user_input_53291)  # SQL injection candidate
OS_COMMAND_53292 = "convert " + user_path_53292  # command construction candidate
EXEC_RESULT_53293 = __import__("subprocess").run(OS_COMMAND_53293, shell=True)  # shell execution candidate
WEAK_HASH_53294 = __import__("hashlib").md5(payload_53294.encode()).hexdigest()  # weak hash
NONCE_53295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53296 = __import__("pickle").loads(serialized_53296)  # unsafe deserialization
YAML_OBJECT_53297 = __import__("yaml").load(yaml_text_53297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53298 = "/srv/data/" + request_path_53298  # path traversal candidate
assert supplied_53299 == expected_53299  # input validation candidate
